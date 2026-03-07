<script lang="ts">
	/**
	 * Admin posts listing page — /admin/posts
	 *
	 * Shows all posts (published and drafts) with status badges.
	 * Links to edit each post. New post button → /admin/posts/new.
	 */
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';

	interface Post {
		id: string;
		slug: string;
		title: string;
		published: boolean;
		published_at: string | null;
		created_at: string;
	}

	let posts: Post[] = $state([]);
	let loading = $state(true);
	let fetchError = $state('');

	function formatDate(iso: string | null): string {
		if (!iso) return '—';
		return new Intl.DateTimeFormat('fr-FR', {
			day: '2-digit',
			month: '2-digit',
			year: 'numeric',
		}).format(new Date(iso));
	}

	function getToken(): string | null {
		const token = sessionStorage.getItem('admin_token');
		if (!token) goto('/admin');
		return token;
	}

	onMount(async () => {
		const token = getToken();
		if (!token) return;

		try {
			// Admin endpoint returns all posts (published + drafts)
			// Uses GET /api/admin/posts — lists all, sorted by created_at desc
			const res = await fetch('/api/admin/posts', {
				headers: { Authorization: `Bearer ${token}` },
			});

			if (res.status === 401 || res.status === 403) {
				sessionStorage.removeItem('admin_token');
				goto('/admin');
				return;
			}

			if (!res.ok) throw new Error(`HTTP ${res.status}`);
			posts = await res.json();
		} catch {
			fetchError = 'Erreur lors du chargement des articles.';
		} finally {
			loading = false;
		}
	});

	function handleLogout() {
		sessionStorage.removeItem('admin_token');
		goto('/admin');
	}
</script>

<svelte:head>
	<title>Articles — Admin Le Jibé</title>
</svelte:head>

<div class="admin-page">
	<header class="admin-nav">
		<a href="/" class="admin-logo">Le <span>Jibé</span></a>
		<nav class="admin-links">
			<a href="/admin/signups" class="admin-link">Inscriptions</a>
			<a href="/admin/posts" class="admin-link active">Articles</a>
		</nav>
		<button class="btn-logout" onclick={handleLogout}>Déconnexion</button>
	</header>

	<main class="admin-main">
		<div class="page-header">
			<h1 class="page-title">Articles</h1>
			<a href="/admin/posts/new" class="btn-new">+ Nouvel article</a>
		</div>

		{#if loading}
			<div class="admin-loading">Chargement…</div>
		{:else if fetchError}
			<div class="admin-error" role="alert">{fetchError}</div>
		{:else if posts.length === 0}
			<div class="admin-empty">
				Aucun article. <a href="/admin/posts/new">Créez le premier →</a>
			</div>
		{:else}
			<div class="table-wrap">
				<table>
					<thead>
						<tr>
							<th>Titre</th>
							<th>Statut</th>
							<th>Publié le</th>
							<th>Créé le</th>
							<th></th>
						</tr>
					</thead>
					<tbody>
						{#each posts as post}
							<tr>
								<td class="title-cell">
									<a href="/admin/posts/{post.id}/edit">{post.title}</a>
								</td>
								<td>
									<span class="status-badge" class:published={post.published}>
										{post.published ? 'Publié' : 'Brouillon'}
									</span>
								</td>
								<td class="date-cell">{formatDate(post.published_at)}</td>
								<td class="date-cell">{formatDate(post.created_at)}</td>
								<td class="action-cell">
									<a href="/admin/posts/{post.id}/edit" class="btn-edit">Modifier</a>
								</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		{/if}
	</main>
</div>

<style>
	.admin-page {
		min-height: 100vh;
		background: var(--ink);
		display: flex;
		flex-direction: column;
	}

	.admin-nav {
		display: flex;
		align-items: center;
		gap: 2rem;
		padding: 1rem 2rem;
		background: var(--ink-soft);
		border-bottom: 1px solid rgba(245, 240, 232, 0.07);
		position: sticky;
		top: 0;
		z-index: 10;
	}

	.admin-logo {
		font-family: var(--f-display);
		font-weight: 800;
		font-size: 1rem;
		color: var(--white);
		letter-spacing: 0.05em;
		margin-right: auto;
	}

	.admin-logo span { color: var(--amber); }

	.admin-links { display: flex; gap: 1.5rem; }

	.admin-link {
		font-family: var(--f-display);
		font-size: 0.75rem;
		font-weight: 600;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: var(--muted);
		transition: color 0.2s;
		padding-bottom: 2px;
	}

	.admin-link:hover, .admin-link.active {
		color: var(--amber-bright);
		border-bottom: 1px solid var(--amber);
	}

	.btn-logout {
		font-family: var(--f-display);
		font-size: 0.7rem;
		font-weight: 600;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: var(--muted);
		background: none;
		border: 1px solid rgba(245, 240, 232, 0.12);
		border-radius: 2px;
		padding: 0.35rem 0.75rem;
		cursor: pointer;
		transition: color 0.2s;
	}

	.btn-logout:hover { color: var(--paper); }

	.admin-main { padding: 2.5rem 2rem; flex: 1; }

	.page-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin-bottom: 2rem;
	}

	.page-title {
		font-family: var(--f-display);
		font-weight: 700;
		font-size: 1.5rem;
		color: var(--white);
	}

	.btn-new {
		font-family: var(--f-display);
		font-size: 0.78rem;
		font-weight: 700;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		padding: 0.6rem 1.25rem;
		background: var(--amber);
		color: var(--ink);
		border-radius: 2px;
		transition: background 0.2s;
	}

	.btn-new:hover { background: var(--amber-bright); }

	.admin-loading, .admin-empty {
		font-size: 0.9rem;
		color: var(--muted);
		padding: 3rem 0;
	}

	.admin-empty a { color: var(--amber); }

	.admin-error {
		color: #e05252;
		font-size: 0.9rem;
		padding: 1rem;
		border: 1px solid rgba(224, 82, 82, 0.3);
		border-radius: 2px;
	}

	.table-wrap {
		overflow-x: auto;
		border: 1px solid rgba(245, 240, 232, 0.07);
		border-radius: 4px;
	}

	table { width: 100%; border-collapse: collapse; font-size: 0.875rem; }

	thead { background: var(--ink-soft); }

	th {
		text-align: left;
		padding: 0.75rem 1rem;
		font-family: var(--f-display);
		font-size: 0.65rem;
		font-weight: 700;
		letter-spacing: 0.15em;
		text-transform: uppercase;
		color: var(--muted);
		border-bottom: 1px solid rgba(245, 240, 232, 0.07);
	}

	td {
		padding: 0.85rem 1rem;
		color: var(--paper-dim);
		border-bottom: 1px solid rgba(245, 240, 232, 0.04);
	}

	tr:last-child td { border-bottom: none; }
	tr:hover td { background: rgba(245, 240, 232, 0.02); }

	.title-cell a {
		color: var(--white);
		font-weight: 500;
		transition: color 0.2s;
	}

	.title-cell a:hover { color: var(--amber-bright); }

	.status-badge {
		font-size: 0.68rem;
		font-family: var(--f-display);
		font-weight: 600;
		letter-spacing: 0.08em;
		text-transform: uppercase;
		padding: 0.2rem 0.5rem;
		border-radius: 2px;
		background: rgba(138, 133, 120, 0.1);
		color: var(--muted);
		border: 1px solid rgba(138, 133, 120, 0.2);
	}

	.status-badge.published {
		background: rgba(212, 134, 10, 0.1);
		color: var(--amber-bright);
		border-color: var(--border);
	}

	.date-cell { color: var(--muted); font-size: 0.8rem; }

	.btn-edit {
		font-size: 0.72rem;
		font-family: var(--f-display);
		font-weight: 600;
		color: var(--amber);
		letter-spacing: 0.06em;
		transition: color 0.2s;
	}

	.btn-edit:hover { color: var(--amber-bright); }
</style>
