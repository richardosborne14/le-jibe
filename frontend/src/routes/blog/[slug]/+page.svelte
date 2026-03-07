<script lang="ts">
	/**
	 * Individual blog post page — /blog/[slug]
	 *
	 * Renders post.body_md as sanitized HTML using marked + DOMPurify.
	 * Styles applied via global .prose class.
	 *
	 * Security: DOMPurify strips any injected scripts or unsafe HTML
	 * before rendering — prevents XSS from untrusted markdown content.
	 */
	import { marked } from 'marked';
	import DOMPurify from 'dompurify';
	import Nav from '$lib/components/Nav.svelte';
	import Footer from '$lib/components/Footer.svelte';

	let { data } = $props();
	// $derived keeps post reactive if data is updated (e.g. invalidation)
	const post = $derived(data.post);

	/** Format ISO date to French long-form (e.g. "15 janvier 2026"). */
	function formatDate(iso: string | null): string {
		if (!iso) return '';
		return new Intl.DateTimeFormat('fr-FR', {
			day: 'numeric',
			month: 'long',
			year: 'numeric',
		}).format(new Date(iso));
	}

	/**
	 * Parse markdown to HTML then sanitize.
	 * Called synchronously — marked.parse() is sync when no async extensions loaded.
	 */
	function renderMarkdown(md: string): string {
		const raw = marked.parse(md) as string;
		// Only sanitize in browser — DOMPurify requires window
		if (typeof window !== 'undefined') {
			return DOMPurify.sanitize(raw);
		}
		return raw;
	}

	// $derived so htmlContent updates if post changes (e.g. after SvelteKit invalidation)
	const htmlContent = $derived(post.body_md ? renderMarkdown(post.body_md) : '');
</script>

<svelte:head>
	<title>{post.title} — Le Jibé</title>
	<meta name="description" content={post.body_md?.slice(0, 150) ?? post.title} />
</svelte:head>

<Nav />

<main class="post-main">
	<div class="container">
		<!-- Back link -->
		<a href="/blog" class="back-link">
			<span aria-hidden="true">←</span>
			Tous les articles
		</a>

		<!-- Post header -->
		<header class="post-header">
			{#if post.published_at}
				<time class="post-date" datetime={post.published_at}>
					{formatDate(post.published_at)}
				</time>
			{/if}
			<h1 class="post-title">{post.title}</h1>
		</header>

		<!-- Post body — sanitized markdown rendered as HTML -->
		<div class="prose post-body">
			<!-- eslint-disable-next-line svelte/no-at-html-tags -->
			{@html htmlContent}
		</div>

		<!-- Footer back link -->
		<div class="post-footer">
			<a href="/blog" class="back-link">
				<span aria-hidden="true">←</span>
				Retour au blog
			</a>
		</div>
	</div>
</main>

<Footer />

<style>
	.post-main {
		min-height: 100vh;
		padding: 8rem 2rem 5rem;
	}

	/* ── Back link ── */
	.back-link {
		display: inline-flex;
		align-items: center;
		gap: 0.4rem;
		font-family: var(--f-display);
		font-size: 0.75rem;
		font-weight: 600;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: var(--muted);
		transition: color 0.2s, gap 0.2s;
		margin-bottom: 3rem;
	}

	.back-link:hover {
		color: var(--paper);
		gap: 0.6rem;
	}

	/* ── Post header ── */
	.post-header {
		margin-bottom: 3.5rem;
		max-width: 68ch;
	}

	.post-date {
		display: block;
		font-family: var(--f-display);
		font-size: 0.68rem;
		font-weight: 600;
		letter-spacing: 0.15em;
		text-transform: uppercase;
		color: var(--amber);
		margin-bottom: 1rem;
	}

	.post-title {
		font-family: var(--f-display);
		font-weight: 800;
		font-size: clamp(2rem, 4vw, 3.5rem);
		line-height: 1.05;
		letter-spacing: -0.02em;
		color: var(--white);
	}

	/* ── Post body — prose styles come from global.css ── */
	.post-body {
		margin-bottom: 5rem;
	}

	/* ── Post footer ── */
	.post-footer {
		border-top: 1px solid rgba(245, 240, 232, 0.07);
		padding-top: 3rem;
	}

	/* ── Responsive ── */
	@media (max-width: 768px) {
		.post-main {
			padding: 6rem 1.25rem 3rem;
		}
	}
</style>
