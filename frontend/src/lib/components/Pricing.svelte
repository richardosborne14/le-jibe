<script lang="ts">
	/**
	 * Pricing section — €9,800 livré.
	 *
	 * Framing: Le Jibé complements the user's primary wheelchair (which
	 * is reimbursed). No reimbursement complexity, no medical paperwork.
	 * Financing mention only — details deferred to Phase 2.
	 *
	 * No road use implication. No medical framing.
	 */
</script>

<section class="pricing">
	<div class="container">
		<div class="pricing-grid">
			<!-- Left: price + CTA -->
			<div class="pricing-left reveal">
				<p class="section-tag">Tarif</p>

				<div class="price-block">
					<div class="price-value">€9 800</div>
					<div class="price-suffix">livré en France métropolitaine</div>
				</div>

				<p class="pricing-note">
					Financement disponible — règlement en plusieurs fois sans frais. Détails à la
					précommande.
				</p>

				<a href="#signup" class="btn-primary pricing-cta">Manifester son intérêt →</a>
			</div>

			<!-- Right: value framing -->
			<div class="pricing-right reveal reveal-delay-2">
				<blockquote class="pricing-quote">
					Votre fauteuil classique reste votre solution principale — remboursée par la Sécurité
					Sociale, adaptée, la vôtre. Le Jibé est votre outil de liberté quotidienne.
				</blockquote>

				<div class="pricing-items">
					<div class="pricing-item">
						<div class="item-check" aria-hidden="true">✓</div>
						<div>
							<div class="item-title">Siège sur mesure inclus</div>
							<div class="item-sub">Pris sur vos mesures corporelles exactes</div>
						</div>
					</div>
					<div class="pricing-item">
						<div class="item-check" aria-hidden="true">✓</div>
						<div>
							<div class="item-title">Pas de cycle de remboursement</div>
							<div class="item-sub">Aucun dossier, aucun délai d'attente</div>
						</div>
					</div>
					<div class="pricing-item">
						<div class="item-check" aria-hidden="true">✓</div>
						<div>
							<div class="item-title">Livraison et mise en service</div>
							<div class="item-sub">Accompagnement à la prise en main inclus</div>
						</div>
					</div>
					<div class="pricing-item">
						<div class="item-check" aria-hidden="true">✓</div>
						<div>
							<div class="item-title">Fabrication française</div>
							<div class="item-sub">Assemblé et ajusté en Dordogne</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<style>
	.pricing {
		padding: 7rem 2rem;
		background: var(--ink-soft);
		position: relative;
		overflow: hidden;
	}

	/* Amber glow from below */
	.pricing::before {
		content: '';
		position: absolute;
		inset: 0;
		background: radial-gradient(
			ellipse 70% 70% at 50% 100%,
			rgba(212, 134, 10, 0.06) 0%,
			transparent 60%
		);
		pointer-events: none;
	}

	.pricing-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 6rem;
		align-items: start;
		position: relative;
		z-index: 1;
	}

	/* ── Price display ── */
	.price-block {
		margin: 2rem 0;
	}

	.price-value {
		font-family: var(--f-display);
		font-weight: 800;
		font-size: clamp(3rem, 5vw, 4.5rem);
		color: var(--white);
		letter-spacing: -0.02em;
		line-height: 1;
	}

	.price-suffix {
		font-size: 0.85rem;
		color: var(--muted);
		margin-top: 0.5rem;
		letter-spacing: 0.04em;
	}

	.pricing-note {
		font-size: 0.9rem;
		color: var(--paper-dim);
		line-height: 1.6;
		margin-bottom: 2rem;
		max-width: 38ch;
	}

	.pricing-cta {
		display: inline-block;
	}

	/* ── Right: quote + checklist ── */
	.pricing-quote {
		font-family: var(--f-serif);
		font-style: italic;
		font-size: 1.1rem;
		line-height: 1.7;
		color: var(--paper-dim);
		border-left: 2px solid var(--amber);
		padding-left: 1.5rem;
		margin-bottom: 2.5rem;
	}

	.pricing-items {
		display: flex;
		flex-direction: column;
		gap: 1.25rem;
	}

	.pricing-item {
		display: flex;
		align-items: flex-start;
		gap: 1rem;
	}

	.item-check {
		color: var(--amber);
		font-family: var(--f-display);
		font-weight: 700;
		font-size: 0.9rem;
		flex-shrink: 0;
		margin-top: 0.1rem;
	}

	.item-title {
		font-family: var(--f-display);
		font-weight: 600;
		font-size: 0.88rem;
		color: var(--white);
		margin-bottom: 0.2rem;
	}

	.item-sub {
		font-size: 0.78rem;
		color: var(--muted);
		line-height: 1.5;
	}

	/* ── Responsive ── */
	@media (max-width: 768px) {
		.pricing-grid {
			grid-template-columns: 1fr;
			gap: 3rem;
		}

		.pricing {
			padding: 5rem 1.25rem;
		}
	}
</style>
