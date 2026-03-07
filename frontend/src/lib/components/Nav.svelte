<script lang="ts">
	/**
	 * Nav — fixed top navigation bar.
	 *
	 * All links are anchor-based for the single-page landing.
	 * Blog and admin are separate routes (full page navigation).
	 */
</script>

<nav>
	<a href="/" class="nav-logo">Le <span>Jibé</span></a>

	<div class="nav-actions">
		<a href="#features" class="nav-link">Le fauteuil</a>
		<a href="#story" class="nav-link">L'histoire</a>
		<a href="/blog" class="nav-link">Blog</a>
		<a href="#signup" class="btn-nav">S'inscrire</a>
	</div>
</nav>

<style>
	nav {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		z-index: 100;
		padding: 0 2rem;
		height: 64px;
		display: flex;
		align-items: center;
		justify-content: space-between;
		/* Gradient fades to transparent so hero background shows through */
		background: linear-gradient(to bottom, rgba(13, 13, 11, 0.95) 0%, rgba(13, 13, 11, 0) 100%);
	}

	.nav-logo {
		font-family: var(--f-display);
		font-weight: 800;
		font-size: 1.25rem;
		letter-spacing: 0.05em;
		color: var(--white);
		display: flex;
		align-items: center;
		gap: 0.25rem;
	}

	.nav-logo span {
		color: var(--amber-bright);
	}

	.nav-actions {
		display: flex;
		align-items: center;
		gap: 2rem;
	}

	.nav-link {
		font-family: var(--f-body);
		font-size: 0.8rem;
		font-weight: 500;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: var(--muted);
		transition: color 0.2s;
	}

	.nav-link:hover {
		color: var(--paper);
	}

	.btn-nav {
		font-family: var(--f-display);
		font-size: 0.75rem;
		font-weight: 700;
		letter-spacing: 0.12em;
		text-transform: uppercase;
		padding: 0.55rem 1.25rem;
		border: 1px solid var(--amber);
		color: var(--amber-bright);
		border-radius: 2px;
		transition: background 0.2s, color 0.2s;
		cursor: pointer;
		background: transparent;
	}

	.btn-nav:hover {
		background: var(--amber);
		color: var(--ink);
	}

	/* On mobile: hide text links, keep just the CTA */
	@media (max-width: 768px) {
		.nav-link {
			display: none;
		}

		nav {
			padding: 0 1.25rem;
		}
	}
</style>
