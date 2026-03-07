<script lang="ts">
	/**
	 * Footer — site-wide footer.
	 *
	 * Includes the required "Destiné à un usage privé" disclaimer.
	 * Contact email and mentions légales are placeholders until JB confirms.
	 */
</script>

<footer>
	<div class="footer-inner container">
		<div class="footer-logo">Le <span>Jibé</span></div>

		<div class="footer-center">
			<p class="footer-copy">© 2026 Le Jibé — Dordogne, France</p>
			<!--
				Required disclaimer — not on checkout yet (Phase 2), but this small
				text in the footer ensures visitors understand the product context.
			-->
			<p class="footer-disclaimer">Destiné à un usage privé.</p>
		</div>

		<div class="footer-links">
			<a href="/blog" class="footer-link">Blog</a>
			<a href="mailto:contact@lejibe.fr" class="footer-link">Contact</a>
			<a href="/mentions-legales" class="footer-link">Mentions légales</a>
		</div>
	</div>
</footer>

<style>
	footer {
		padding: 3rem 2rem;
		border-top: 1px solid rgba(245, 240, 232, 0.06);
	}

	.footer-inner {
		display: flex;
		align-items: center;
		justify-content: space-between;
		flex-wrap: wrap;
		gap: 1.5rem;
	}

	.footer-logo {
		font-family: var(--f-display);
		font-weight: 800;
		font-size: 1rem;
		letter-spacing: 0.05em;
		color: var(--white);
	}

	.footer-logo span {
		color: var(--amber);
	}

	.footer-center {
		text-align: center;
	}

	.footer-copy {
		font-size: 0.72rem;
		color: var(--muted);
	}

	/* Small print — no emphasis, just there for transparency */
	.footer-disclaimer {
		font-size: 0.68rem;
		color: rgba(138, 133, 120, 0.6);
		margin-top: 0.25rem;
	}

	.footer-links {
		display: flex;
		gap: 1.5rem;
	}

	.footer-link {
		font-size: 0.72rem;
		letter-spacing: 0.08em;
		text-transform: uppercase;
		color: var(--muted);
		transition: color 0.2s;
	}

	.footer-link:hover {
		color: var(--paper);
	}

	/* ── Responsive ── */
	@media (max-width: 768px) {
		.footer-inner {
			flex-direction: column;
			text-align: center;
		}

		.footer-links {
			justify-content: center;
		}

		footer {
			padding: 2.5rem 1.25rem;
		}
	}
</style>
