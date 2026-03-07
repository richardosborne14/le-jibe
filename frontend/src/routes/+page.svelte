<script lang="ts">
	/**
	 * Landing page — root route (/).
	 *
	 * Assembles all section components in narrative order:
	 *  1. Hero — hook
	 *  2. Ticker — brand strip
	 *  3. Problem — why existing options fail
	 *  4. Story — JB's origin
	 *  5. Features — complete device description
	 *  6. Pricing — €9,800, "outil de liberté" framing
	 *  7. Signup — interest capture (Task 5)
	 *  8. Footer
	 *
	 * Chat widget placeholder (bottom-right) is included here.
	 * Real widget implemented in Task 9.
	 */
	import Nav from '$lib/components/Nav.svelte';
	import Hero from '$lib/components/Hero.svelte';
	import Ticker from '$lib/components/Ticker.svelte';
	import Problem from '$lib/components/Problem.svelte';
	import Story from '$lib/components/Story.svelte';
	import Features from '$lib/components/Features.svelte';
	import Pricing from '$lib/components/Pricing.svelte';
	import SignupForm from '$lib/components/SignupForm.svelte';
	import Footer from '$lib/components/Footer.svelte';
</script>

<svelte:head>
	<title>Le Jibé — Liberté de mouvement</title>
</svelte:head>

<Nav />

<main>
	<Hero />
	<Ticker />
	<Problem />
	<Story />
	<Features />
	<Pricing />

	<!-- ── Signup section ──────────────────────────────────────────────
	     Anchor #signup used by nav CTA and all "Manifester son intérêt" links.
	     SignupForm component handles all API interaction (Task 5).
	     ───────────────────────────────────────────────────────────────── -->
	<section class="signup-section" id="signup">
		<div class="signup-inner">
			<div class="signup-header">
				<p class="section-tag signup-tag">Pré-lancement</p>
				<h2 class="section-title">
					Soyez parmi<br />
					les <em>premiers informés.</em>
				</h2>
				<p class="signup-sub">
					Pas d'engagement. On vous écrit quand Le Jibé sera disponible à la précommande.
				</p>
			</div>

			<SignupForm />
		</div>
	</section>
</main>

<Footer />

<!--
	Chat widget placeholder — bottom-right floating button.
	Real AI chat widget implemented in Task 9 (RAG + Claude).
	Placeholder ensures layout space is reserved now.
-->
<div class="chat-placeholder" aria-hidden="true" title="Chat — disponible bientôt">
	<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
		<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
	</svg>
</div>

<style>
	main {
		/* Nav is fixed so main content starts below it */
		padding-top: 0;
	}

	/* ── Signup section wrapper ── */
	.signup-section {
		padding: 7rem 2rem;
		background: var(--ink-soft);
		position: relative;
		overflow: hidden;
	}

	/* Ambient glow behind the form */
	.signup-section::before {
		content: '';
		position: absolute;
		inset: 0;
		background: radial-gradient(
			ellipse 70% 70% at 50% 100%,
			rgba(212, 134, 10, 0.08) 0%,
			transparent 60%
		);
		pointer-events: none;
	}

	.signup-inner {
		position: relative;
		z-index: 1;
		max-width: 640px;
		margin: 0 auto;
		text-align: center;
	}

	.signup-header {
		margin-bottom: 3rem;
	}

	/* Override section-tag to centre without the left pseudo-element */
	.signup-tag {
		justify-content: center;
	}

	.signup-tag::before {
		display: none;
	}

	.signup-sub {
		font-size: 1rem;
		color: var(--muted);
		margin-top: 1rem;
		line-height: 1.7;
	}

	/* ── Chat placeholder — bottom-right floating button ── */
	.chat-placeholder {
		position: fixed;
		bottom: 1.5rem;
		right: 1.5rem;
		z-index: 50;
		width: 52px;
		height: 52px;
		border-radius: 50%;
		background: var(--amber);
		color: var(--ink);
		display: flex;
		align-items: center;
		justify-content: center;
		cursor: default;
		opacity: 0.5; /* Dimmed — not yet interactive */
		box-shadow: 0 4px 20px rgba(212, 134, 10, 0.3);
	}

	.chat-placeholder svg {
		width: 22px;
		height: 22px;
	}

	/* ── Responsive ── */
	@media (max-width: 768px) {
		.signup-section {
			padding: 5rem 1.25rem;
		}
	}
</style>
