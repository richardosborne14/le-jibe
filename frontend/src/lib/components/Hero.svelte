<script lang="ts">
	/**
	 * Hero section — first thing the visitor sees.
	 *
	 * Layout: headline + capability badges + CTA (left), video placeholder (right).
	 *
	 * CRITICAL rules enforced here:
	 *  - No speed figures (no 30km/h, no "rapide")
	 *  - No road context (no "sur route", "en ville")
	 *  - Stats strip removed — replaced by capability badges
	 *  - Video is a placeholder div; real YouTube URL comes from JB later
	 */
</script>

<section class="hero">
	<!-- Ambient background gradient — gives depth without images -->
	<div class="hero-bg" aria-hidden="true"></div>

	<div class="hero-content">
		<!-- Left column: headline + badges + CTA -->
		<div class="hero-left">
			<p class="hero-eyebrow">Dordogne, France — Conçu par un utilisateur</p>

			<h1 class="hero-headline">
				Liberté<br />
				<em>sans</em><br />
				compromis.
			</h1>

			<p class="hero-sub">
				Le Jibé est un dispositif de mobilité électrique complet — base gyroscopique tout-terrain,
				siège carbone sur mesure, roue stabilisatrice et joystick. Conçu de l'intérieur par
				quelqu'un qui en avait besoin.
			</p>

			<div class="hero-cta-group">
				<a href="#signup" class="btn-primary">Manifester son intérêt</a>
				<span class="cta-note">Aucun engagement — premiers informés à la sortie</span>
			</div>

			<!--
				Capability badges — replace the original speed/range stat strip.
				These describe what the device does, not how fast it goes.
			-->
			<div class="hero-badges">
				<span class="badge">Tout-terrain</span>
				<span class="badge">Siège sur mesure</span>
				<span class="badge">Roue stabilisatrice</span>
				<span class="badge">Contrôle par joystick</span>
			</div>
		</div>

		<!-- Right column: video placeholder — real URL from JB, Phase 1 content pipeline -->
		<div class="hero-video-col">
			<div class="video-frame" aria-label="Vidéo de démonstration — à venir">
				<div class="video-frame-inner">
					<div class="video-play" aria-hidden="true">
						<svg viewBox="0 0 24 24" aria-hidden="true">
							<path d="M8 5v14l11-7z" />
						</svg>
					</div>
				</div>
				<div class="video-label">Vidéo de démonstration</div>
			</div>
			<p class="video-caption">JB dans son quotidien — herbe, graviers, couloirs, pavés.</p>
		</div>
	</div>
</section>

<style>
	.hero {
		min-height: 100svh;
		display: grid;
		grid-template-rows: 1fr auto;
		position: relative;
		overflow: hidden;
	}

	/* Atmospheric amber glow — no images needed */
	.hero-bg {
		position: absolute;
		inset: 0;
		background:
			radial-gradient(ellipse 80% 60% at 60% 40%, rgba(212, 134, 10, 0.12) 0%, transparent 60%),
			radial-gradient(ellipse 40% 40% at 20% 80%, rgba(212, 134, 10, 0.06) 0%, transparent 50%),
			var(--ink);
	}

	/* Subtle vertical line accent — pure CSS, no SVG */
	.hero-bg::after {
		content: '';
		position: absolute;
		top: 0;
		right: 20%;
		width: 1px;
		height: 100%;
		background: linear-gradient(
			to bottom,
			transparent 0%,
			var(--border) 30%,
			var(--border) 70%,
			transparent 100%
		);
	}

	.hero-content {
		position: relative;
		z-index: 2;
		max-width: var(--max);
		margin: 0 auto;
		width: 100%;
		padding: 9rem 2rem 5rem;
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 4rem;
		align-items: center;
	}

	/* ── Hero left animations (staggered fade-up on load) ── */
	.hero-left > * {
		opacity: 0;
		transform: translateY(20px);
		animation: fadeUp 0.8s var(--ease) forwards;
	}

	.hero-eyebrow   { animation-delay: 0.1s; }
	.hero-headline  { animation-delay: 0.25s; }
	.hero-sub       { animation-delay: 0.4s; }
	.hero-cta-group { animation-delay: 0.55s; }
	.hero-badges    { animation-delay: 0.7s; }

	.hero-video-col {
		opacity: 0;
		animation: fadeUp 0.9s 0.4s var(--ease) forwards;
	}

	@keyframes fadeUp {
		to { opacity: 1; transform: none; }
	}

	/* ── Typography ── */
	.hero-eyebrow {
		font-family: var(--f-body);
		font-size: 0.7rem;
		font-weight: 600;
		letter-spacing: 0.2em;
		text-transform: uppercase;
		color: var(--amber-bright);
		margin-bottom: 1.25rem;
		display: flex;
		align-items: center;
		gap: 0.75rem;
	}

	.hero-eyebrow::before {
		content: '';
		display: block;
		width: 2rem;
		height: 1px;
		background: var(--amber);
		flex-shrink: 0;
	}

	.hero-headline {
		font-family: var(--f-display);
		font-weight: 800;
		font-size: clamp(3rem, 6vw, 5.5rem);
		line-height: 0.95;
		letter-spacing: -0.02em;
		color: var(--white);
		margin-bottom: 0.5rem;
	}

	.hero-headline em {
		font-style: italic;
		font-family: var(--f-serif);
		font-weight: 400;
		color: var(--amber-pale);
	}

	.hero-sub {
		font-family: var(--f-body);
		font-size: 1.05rem;
		line-height: 1.65;
		color: var(--paper-dim);
		max-width: 42ch;
		margin-top: 1.75rem;
		margin-bottom: 2.5rem;
	}

	.hero-cta-group {
		display: flex;
		align-items: center;
		gap: 1.5rem;
		flex-wrap: wrap;
	}

	.cta-note {
		font-size: 0.78rem;
		color: var(--muted);
		letter-spacing: 0.02em;
	}

	/* ── Capability badges — replaces speed stat strip ── */
	.hero-badges {
		display: flex;
		flex-wrap: wrap;
		gap: 0.6rem;
		padding-top: 2.5rem;
		border-top: 1px solid rgba(245, 240, 232, 0.08);
	}

	.badge {
		font-family: var(--f-display);
		font-size: 0.68rem;
		font-weight: 600;
		letter-spacing: 0.12em;
		text-transform: uppercase;
		color: var(--amber-bright);
		border: 1px solid var(--border);
		border-radius: 2px;
		padding: 0.35rem 0.75rem;
		background: rgba(212, 134, 10, 0.05);
	}

	/* ── Video placeholder ── */
	.hero-video-col {
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.video-frame {
		position: relative;
		width: 100%;
		aspect-ratio: 16 / 9;
		background: var(--ink-soft);
		border: 1px solid rgba(212, 134, 10, 0.2);
		border-radius: 4px;
		overflow: hidden;
		cursor: pointer;
	}

	.video-frame-inner {
		position: absolute;
		inset: 0;
		background:
			linear-gradient(135deg, rgba(212, 134, 10, 0.08) 0%, transparent 50%),
			repeating-linear-gradient(
				-45deg,
				transparent,
				transparent 40px,
				rgba(212, 134, 10, 0.02) 40px,
				rgba(212, 134, 10, 0.02) 41px
			),
			var(--ink-soft);
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.video-play {
		width: 64px;
		height: 64px;
		border-radius: 50%;
		background: rgba(212, 134, 10, 0.15);
		border: 2px solid var(--amber);
		display: flex;
		align-items: center;
		justify-content: center;
		transition: background 0.2s, transform 0.15s;
	}

	.video-frame:hover .video-play {
		background: rgba(212, 134, 10, 0.3);
		transform: scale(1.05);
	}

	.video-play svg {
		width: 22px;
		height: 22px;
		fill: var(--amber-bright);
		margin-left: 3px; /* optical centering for play triangle */
	}

	.video-label {
		position: absolute;
		bottom: 1rem;
		left: 1rem;
		font-size: 0.7rem;
		letter-spacing: 0.12em;
		text-transform: uppercase;
		color: var(--paper-dim);
	}

	.video-caption {
		font-size: 0.78rem;
		color: var(--muted);
		font-style: italic;
	}

	/* ── Responsive ── */
	@media (max-width: 768px) {
		.hero-content {
			grid-template-columns: 1fr;
			padding: 7rem 1.25rem 3rem;
			gap: 3rem;
		}

		.hero-video-col {
			order: -1; /* Video above headline on mobile */
		}

		.hero-headline {
			font-size: clamp(2.5rem, 10vw, 3.5rem);
		}
	}
</style>
