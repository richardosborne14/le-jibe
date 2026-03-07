/**
 * Load function for the post edit page — /admin/posts/[id]/edit
 *
 * Fetches the post from GET /api/admin/posts/{id}.
 * The admin endpoint returns both published and draft posts.
 * Token is read from sessionStorage (client-side only).
 *
 * Note: Because token auth is client-side only, this load function
 * runs on the client. A missing post returns 404.
 */
import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';

export const ssr = false; // Admin is client-only — token in sessionStorage

export const load: PageLoad = async ({ params, fetch }) => {
	const token = typeof window !== 'undefined'
		? sessionStorage.getItem('admin_token')
		: null;

	if (!token) {
		// Will be caught by the layout auth guard
		return { post: null };
	}

	const response = await fetch(`/api/admin/posts/${params.id}`, {
		headers: { Authorization: `Bearer ${token}` },
	});

	if (response.status === 404) {
		throw error(404, 'Article introuvable.');
	}

	if (!response.ok) {
		throw error(response.status, `Erreur de chargement (${response.status}).`);
	}

	const post = await response.json();
	return { post };
};
