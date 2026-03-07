<script lang="ts">
	/**
	 * Blog listing page — /blog
	 *
	 * Fetches all published posts from GET /api/posts.
	 * Displays as cards: title, French-formatted date, excerpt.
	 * Empty state shown if no posts are published yet.
	 */
	import { onMount } from 'svelte';
	import Nav from '$lib/components/Nav.svelte';
	import Footer from '$lib/components/Footer.svelte';

	interface Post {
		id: string;
		slug: string;
		title: string;
		published_at: string | null;
		excerpt: string | null;
	}

	let posts: Post[] = $state([]);
	let loading = $state(true);
	let fetchError = $state('');

	/** Format an ISO date string to French long-form date (e.g. "15 janvier 2026"). */
	function formatDate(iso: string | null): string {
		if (!iso) return '';
		return new Intl.DateTimeFormat('fr-FR', {
			day: 'numeric',
			month: 'long',
			year: 'numeric',
		}).format(new Date(iso));
	}

	onMount(async () => {
		try {
			const res = await fetch('/api/posts');
			if (!res.ok) throw new Error(`HTTP ${res.status}`);
			posts = await res.json();
		} catch {
			fetchError = 'Impossible de charger les articles. Réessayez plus tard.';
		} finally {
			loading = false;
		}
	});
</script>

<svelte:head>
	<title>Blog — Le Jibé</title>
	<meta
		name="description"
		content="Articles sur Le Jibé — développement, histoire, mobilité et vie quotidienne avec le dispositif."
	/>
</svelte:head>

<Nav />

<main class="blog-main">
	<div class="container">
		<!-- Page header -->
		<header class="blog-header">
			<p class="section-tag">Journal</p>
			<h1 class="section-title">
				Le blog<br />
				<em>Le Jibé.</em>
			</h1>
			<p class="blog-sub">
				Développement, usage quotidien, et tout ce qui mène à un fauteuil conçu de l'intérieur.
			</p>
		</header>

		<!-- Loading skeleton -->
		{#if loading}
			<div class="blog-loading" aria-busy="true" aria-label="Chargement des articles">
				{#each [1, 2, 3] as _}
					<div class="post-skeleton">
						<div class="skeleton-date"></div>
						<div class="skeleton-title"></div>
						<div class="skeleton-excerpt"></div>
					</div>
				{/each}
			</div>

		<!-- Error state -->
		{:else if fetchError}
			<div class="blog-error" role="alert">{fetchError}</div>

		<!-- Empty state -->
		{:else if posts.length === 0}
			<div class="blog-empty">
				<p class="empty-msg">Aucun article pour le moment. Revenez bientôt !</p>
			</div>

		<!-- Post list -->
		{:else}
			<div class="post-list">
				{#each posts as post}
					<article class="post-card reveal">
						{#if post.published_at}
							<time class="post-date" datetime={post.published_at}>
								{formatDate(post.published_at)}
							</time>
						{/if}

						<h2 class="post-title">
							<a href="/blog/{post.slug}">{post.title}</a>
						</h2>

						{#if post.excerpt}
							<p class="post-excerpt">{post.excerpt}</p>
						{/if}

						<a href="/blog/{post.slug}" class="post-read-more">
							Lire l'article
							<span aria-hidden="true">→</span>
						</a>
					</article>
				{/each}
			</div>
		{/if}
	</div>
</main>

<Footer />

<style>
	.blog-main {
		min-height: 100vh;
		padding: 8rem 2rem 5rem;
	}

	/* ── Header ── */
	.blog-header {
		max-width: 600px;
		margin-bottom: 5rem;
	}

	.blog-sub {
		margin-top: 1.5rem;
		font-size: 1rem;
		color: var(--muted);
		line-height: 1.7;
		max-width: 50ch;
	}

	/* ── Loading skeletons ── */
	.blog-loading {
		display: flex;
		flex-direction: column;
		gap: 3rem;
	}

	.post-skeleton {
		padding: 2rem 0;
		border-bottom: 1px solid rgba(245, 240, 232, 0.07);
	}

	.skeleton-date,
	.skeleton-title,
	.skeleton-excerpt {
		background: rgba(245, 240, 232, 0.06);
		border-radius: 2px;
		animation: shimmer 1.5s infinite;
	}

	.skeleton-date { width: 120px; height: 12px; margin-bottom: 1rem; }
	.skeleton-title { width: 70%; height: 24px; margin-bottom: 0.75rem; }
	.skeleton-excerpt { width: 90%; height: 14px; }

	@keyframes shimmer {
		0%, 100% { opacity: 0.5; }
		50% { opacity: 1; }
	}

	/* ── Error / empty ── */
	.blog-error {
		padding: 1.5rem;
		border: 1px solid rgba(224, 82, 82, 0.3);
		border-radius: 2px;
		color: #e05252;
		font-size: 0.9rem;
	}

	.blog-empty {
		padding: 4rem 0;
		text-align: center;
	}

	.empty-msg {
		font-family: var(--f-serif);
		font-style: italic;
		font-size: 1.1rem;
		color: var(--muted);
	}

	/* ── Post list ── */
	.post-list {
		display: flex;
		flex-direction: column;
		gap: 0;
	}

	.post-card {
		padding: 3rem 0;
		border-bottom: 1px solid rgba(245, 240, 232, 0.07);
		display: grid;
		grid-template-columns: 140px 1fr;
		grid-template-rows: auto auto auto;
		gap: 0.5rem 2rem;
		align-items: start;
	}

	.post-card:first-child {
		border-top: 1px solid rgba(245, 240, 232, 0.07);
	}

	.post-date {
		font-family: var(--f-display);
		font-size: 0.68rem;
		font-weight: 600;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: var(--amber);
		grid-column: 1;
		grid-row: 1;
		padding-top: 0.2rem;
	}

	.post-title {
		font-family: var(--f-display);
		font-weight: 700;
		font-size: clamp(1.2rem, 2.5vw, 1.75rem);
		line-height: 1.2;
		color: var(--white);
		grid-column: 2;
		grid-row: 1;
	}

	.post-title a {
		transition: color 0.2s;
	}

	.post-title a:hover {
		color: var(--amber-bright);
	}

	.post-excerpt {
		font-size: 0.9rem;
		color: var(--muted);
		line-height: 1.65;
		grid-column: 2;
		grid-row: 2;
		max-width: 60ch;
	}

	.post-read-more {
		grid-column: 2;
		grid-row: 3;
		font-family: var(--f-display);
		font-size: 0.75rem;
		font-weight: 600;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: var(--amber);
		margin-top: 0.5rem;
		display: inline-flex;
		align-items: center;
		gap: 0.4rem;
		transition: gap 0.2s;
	}

	.post-read-more:hover {
		gap: 0.6rem;
	}

	/* ── Responsive ── */
	@media (max-width: 768px) {
		.blog-main {
			padding: 6rem 1.25rem 3rem;
		}

		.post-card {
			grid-template-columns: 1fr;
		}

		.post-date,
		.post-title,
		.post-excerpt,
		.post-read-more {
			grid-column: 1;
		}

		.post-date {
			grid-row: 1;
		}

		.post-title {
			grid-row: 2;
		}

		.post-excerpt {
			grid-row: 3;
		}

		.post-read-more {
			grid-row: 4;
		}
	}
</style>
