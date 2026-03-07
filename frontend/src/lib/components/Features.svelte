<script lang="ts">
	/**
	 * Features section — three cards describing the complete device.
	 *
	 * Framing: "complete device" — not "detachable base" or "add-on".
	 * Card 1 emphasises the front stabilising wheel (key differentiator).
	 * NO speed figures anywhere. NO road context.
	 */

	const features = [
		{
			num: '01',
			title: 'Base Segway + roue stabilisatrice',
			desc:
				"Grandes roues tout-terrain avec stabilisation gyroscopique. La roue avant réduit drastiquement le risque de chute sur sol inégal. Franchit les bordures et petits obstacles. Herbe, graviers, carrelage, surfaces irrégulières — sans y penser.",
			icon: `<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
				<circle cx="20" cy="24" r="8"/>
				<circle cx="8" cy="28" r="4"/>
				<path d="M16 24 L12 28"/>
				<path d="M20 16 L20 6"/>
				<path d="M14 10 L26 10"/>
			</svg>`,
		},
		{
			num: '02',
			title: 'Siège carbone sur mesure',
			desc:
				"Imprimé en 3D sur les mesures exactes du corps de l'utilisateur. Côtés plats ou avec appuis latéraux — configuré selon le mode de transfert et la stabilité du tronc. L'utilisateur conserve son propre coussin. Léger, robuste, confortable une journée entière.",
			icon: `<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
				<path d="M10 32 L10 14 Q10 10 14 10 L26 10 Q30 10 30 14 L30 32"/>
				<path d="M8 32 L32 32"/>
				<path d="M16 10 L16 22"/>
				<path d="M24 10 L24 22"/>
			</svg>`,
		},
		{
			num: '03',
			title: 'Joystick & contrôle intuitif',
			desc:
				"Monture rigide d'un côté du cadre. Une légère poussée incline le cadre — le Segway se déplace dans cette direction. Les mouvements du corps ne causent aucun déplacement involontaire. Rotation à 360° sur place. Contrôle naturel en quelques minutes.",
			icon: `<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
				<circle cx="20" cy="16" r="5"/>
				<line x1="20" y1="21" x2="20" y2="34"/>
				<path d="M12 28 L28 28"/>
				<circle cx="20" cy="16" r="2" fill="currentColor" stroke="none"/>
			</svg>`,
		},
	];
</script>

<section class="features" id="features">
	<div class="container">
		<div class="features-header reveal">
			<div>
				<p class="section-tag">Le fauteuil</p>
				<h2 class="section-title">
					Conçu pour<br />
					<em>la vraie vie.</em>
				</h2>
			</div>
			<p class="features-intro">
				Pas un compromis entre mobilité et confort. Pas une concession entre intérieur et extérieur.
				Le Jibé fait les deux — parce qu'un utilisateur réel en avait besoin.
			</p>
		</div>

		<div class="features-grid">
			{#each features as feature, i}
				<div class="feature-card reveal reveal-delay-{i + 1}">
					<div class="feature-num">{feature.num}</div>

					<!-- eslint-disable-next-line svelte/no-at-html-tags -->
					<div class="feature-icon">{@html feature.icon}</div>

					<h3 class="feature-title">{feature.title}</h3>
					<p class="feature-desc">{feature.desc}</p>
				</div>
			{/each}
		</div>
	</div>
</section>

<style>
	.features {
		padding: 7rem 2rem;
		position: relative;
	}

	.features-header {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 4rem;
		margin-bottom: 5rem;
		align-items: end;
	}

	.features-intro {
		font-size: 1rem;
		color: var(--muted);
		line-height: 1.7;
		max-width: 40ch;
	}

	/* Three-column card grid separated by hairline borders */
	.features-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 1px;
		background: rgba(245, 240, 232, 0.06);
		border: 1px solid rgba(245, 240, 232, 0.06);
	}

	.feature-card {
		background: var(--ink);
		padding: 2.5rem 2rem;
		position: relative;
		transition: background 0.25s;
	}

	.feature-card:hover {
		background: var(--ink-soft);
	}

	/* Amber underline appears on hover */
	.feature-card::after {
		content: '';
		position: absolute;
		bottom: 0;
		left: 2rem;
		right: 2rem;
		height: 1px;
		background: linear-gradient(to right, var(--amber), transparent);
		opacity: 0;
		transition: opacity 0.25s;
	}

	.feature-card:hover::after {
		opacity: 1;
	}

	.feature-num {
		font-family: var(--f-display);
		font-size: 0.6rem;
		font-weight: 700;
		letter-spacing: 0.15em;
		color: var(--amber);
		margin-bottom: 1.5rem;
	}

	/* SVG icon injected via @html — styled via currentColor */
	.feature-icon {
		width: 40px;
		height: 40px;
		margin-bottom: 1.25rem;
		color: var(--amber);
	}

	:global(.feature-icon svg) {
		width: 100%;
		height: 100%;
	}

	.feature-title {
		font-family: var(--f-display);
		font-weight: 700;
		font-size: 1.05rem;
		color: var(--white);
		margin-bottom: 0.75rem;
		line-height: 1.25;
	}

	.feature-desc {
		font-size: 0.88rem;
		color: var(--muted);
		line-height: 1.65;
	}

	/* ── Responsive ── */
	@media (max-width: 768px) {
		.features-header {
			grid-template-columns: 1fr;
			gap: 1.5rem;
			margin-bottom: 3rem;
		}

		.features-grid {
			grid-template-columns: 1fr;
		}

		.features {
			padding: 5rem 1.25rem;
		}
	}
</style>
