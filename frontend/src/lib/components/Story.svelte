<script lang="ts">
	/**
	 * Story section — JB's origin narrative.
	 *
	 * Complete device framing: JB built the whole thing, not an add-on.
	 * Tone: direct and factual. The story sells itself — no inspiration-porn.
	 *
	 * No speed figures. No road context. No medical language.
	 */
</script>

<section class="story" id="story">
	<div class="container">
		<div class="story-grid">
			<!-- Photo placeholder — JB provides real photo later -->
			<div class="story-image-col reveal">
				<div class="story-img-placeholder" aria-label="Photo de JB — à venir">
					<div class="img-inner">
						<span class="img-label">Photo de JB<br />à venir</span>
					</div>
				</div>
				<!-- Vertical label — editorial detail -->
				<div class="story-tag-vertical" aria-hidden="true">Le Jibé — Dordogne</div>
			</div>

			<!-- Text content -->
			<div class="story-text reveal reveal-delay-2">
				<p class="section-tag">L'origine</p>
				<h2 class="section-title">
					Je l'ai construit<br />
					parce que <em>rien<br />d'autre ne marchait.</em>
				</h2>

				<p class="story-body">
					JB est ingénieur. Il est aussi paraplégique. Après des années à chercher un engin qui
					corresponde réellement à sa vie quotidienne — ses transferts, ses terrains, son coffre de
					voiture — il a arrêté de chercher.
				</p>

				<p class="story-body">
					Il a pris une base Segway. Un siège imprimé en carbone sur mesure. Un joystick monté
					rigide. Et il a assemblé quelque chose qui n'existait pas : un dispositif de mobilité
					conçu de l'intérieur, par quelqu'un qui sait ce que "fonctionnel" veut dire dans la vraie
					vie.
				</p>

				<p class="story-body">
					Le Jibé n'est pas un produit médical. <strong>C'est un outil de liberté.</strong> La
					différence, c'est que celui qui l'a conçu l'utilise chaque jour.
				</p>

				<div class="story-signature">
					<div class="sig-avatar" aria-hidden="true">JB</div>
					<div class="sig-text">
						<div class="sig-name">Jean-Baptiste</div>
						<div class="sig-role">Fondateur, ingénieur & premier utilisateur — Dordogne, France</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<style>
	.story {
		padding: 7rem 2rem;
		background: var(--ink-soft);
		position: relative;
		overflow: hidden;
	}

	/* Subtle gradient border at top */
	.story::before {
		content: '';
		position: absolute;
		top: -1px;
		left: 0;
		right: 0;
		height: 1px;
		background: linear-gradient(to right, transparent, var(--border), transparent);
	}

	.story-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 6rem;
		align-items: center;
	}

	/* ── Image column ── */
	.story-image-col {
		position: relative;
	}

	.story-img-placeholder {
		aspect-ratio: 3 / 4;
		background: var(--ink);
		border: 1px solid rgba(245, 240, 232, 0.08);
		border-radius: 4px;
		position: relative;
		overflow: hidden;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	/* Amber glow inside placeholder */
	.story-img-placeholder::before {
		content: '';
		position: absolute;
		inset: 0;
		background: radial-gradient(
			ellipse 60% 60% at 50% 60%,
			rgba(212, 134, 10, 0.1) 0%,
			transparent 70%
		);
	}

	.img-inner {
		position: relative;
		z-index: 1;
		text-align: center;
	}

	.img-label {
		font-family: var(--f-display);
		font-size: 0.65rem;
		letter-spacing: 0.2em;
		text-transform: uppercase;
		color: var(--muted);
		line-height: 1.8;
	}

	/* Rotated label beside the photo — decorative editorial detail */
	.story-tag-vertical {
		position: absolute;
		right: -1.75rem;
		top: 50%;
		transform: translateY(-50%) rotate(90deg);
		font-size: 0.6rem;
		letter-spacing: 0.2em;
		text-transform: uppercase;
		color: rgba(212, 134, 10, 0.4);
		font-family: var(--f-display);
		font-weight: 600;
		white-space: nowrap;
	}

	/* ── Text column ── */
	.story-text .section-title {
		margin-bottom: 2rem;
	}

	.story-body {
		font-family: var(--f-serif);
		font-size: 1.1rem;
		line-height: 1.75;
		color: var(--paper-dim);
		margin-bottom: 1.5rem;
	}

	.story-body strong {
		color: var(--white);
		font-weight: 400; /* Serif bold is too heavy — normal weight looks better */
	}

	/* Signature block — JB attribution */
	.story-signature {
		margin-top: 2.5rem;
		padding-top: 1.5rem;
		border-top: 1px solid rgba(245, 240, 232, 0.08);
		display: flex;
		align-items: center;
		gap: 1rem;
	}

	.sig-avatar {
		width: 48px;
		height: 48px;
		border-radius: 50%;
		background: var(--ink);
		border: 1px solid var(--border);
		display: flex;
		align-items: center;
		justify-content: center;
		font-family: var(--f-display);
		font-weight: 800;
		font-size: 1rem;
		color: var(--amber);
		flex-shrink: 0;
	}

	.sig-name {
		font-family: var(--f-display);
		font-weight: 700;
		font-size: 0.85rem;
		color: var(--white);
	}

	.sig-role {
		font-size: 0.72rem;
		color: var(--muted);
		letter-spacing: 0.05em;
		margin-top: 0.1rem;
	}

	/* ── Responsive ── */
	@media (max-width: 768px) {
		.story-grid {
			grid-template-columns: 1fr;
			gap: 3rem;
		}

		.story-tag-vertical {
			display: none; /* No room for the rotated label on mobile */
		}

		.story {
			padding: 5rem 1.25rem;
		}
	}
</style>
