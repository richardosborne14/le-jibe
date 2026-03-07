/**
 * Load function for individual blog post pages — /blog/[slug]
 *
 * Fetches the post from GET /api/posts/{slug}.
 * Returns 404 via SvelteKit's error() helper if not found.
 * Data is passed to the +page.svelte component as `data.post`.
 */
import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ params, fetch }) => {
	const response = await fetch(`/api/posts/${params.slug}`);

	if (response.status === 404) {
		// SvelteKit renders the nearest +error.svelte with this
		throw error(404, 'Article introuvable.');
	}

	if (!response.ok) {
		throw error(500, 'Erreur lors du chargement de l\'article.');
	}

	const post = await response.json();

	return { post };
};
