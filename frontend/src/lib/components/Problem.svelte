<script lang="ts">
	/**
	 * Problem section — explains WHY Le Jibé exists.
	 *
	 * This is editorial prose, not a bullet list. The goal is to make the
	 * reader feel understood before we present the solution.
	 *
	 * Tone: factual, direct. No medical language. No road context.
	 * We describe the user's physical reality without dramatising it.
	 */
</script>

<section class="problem">
	<div class="container">
		<div class="problem-grid">
			<!-- Left: section label + headline -->
			<div class="problem-left reveal">
				<p class="section-tag">Le constat</p>
				<h2 class="section-title">
					Chaque alternative<br />
					impose un <em>compromis.</em>
				</h2>

				<!-- Visual accent — amber rule line -->
				<div class="problem-rule" aria-hidden="true"></div>

				<p class="problem-pullquote">
					"Votre fauteuil vous convient. Le problème, c'est le reste."
				</p>
			</div>

			<!-- Right: editorial prose -->
			<div class="problem-right reveal reveal-delay-2">
				<p class="problem-body">
					Les fauteuils électriques classiques n'ont pas de roue avant stabilisatrice. L'utilisateur
					penche en avant, en arrière, sur le côté — et le fauteuil suit. Sur une surface inégale, le
					risque de chute est réel. Un seul modèle en France dispose de cette roue. Il n'a pas de
					propulsion électrique.
				</p>

				<p class="problem-body">
					Les alternatives à trois roues avec propulsion coûtent le double. Leurs sièges inclinés
					sont conçus pour faciliter la poussée manuelle — pas pour les utilisateurs qui ont besoin
					de transferts plats. Pour beaucoup, s'y asseoir seul est impossible.
				</p>

				<p class="problem-body">
					Ces appareils pèsent entre 80 et 120 kg. Charger seul dans un coffre de voiture : exclu.
					Et si au bout de six mois ce n'est pas la bonne solution, vous êtes engagé pour cinq ans
					— le cycle de remboursement recommence à zéro.
				</p>

				<!-- The pivot — Le Jibé's answer, introduced naturally -->
				<div class="problem-answer">
					<div class="answer-line" aria-hidden="true"></div>
					<p class="answer-text">
						Le Jibé part d'une idée différente. Votre fauteuil classique reste votre solution
						principale — remboursée, adaptée, la vôtre. Le Jibé est votre second engin : celui qui
						transforme votre quotidien. Siège taillé sur votre corps. Roue avant pour la stabilité.
						Joystick pour que vos mains et votre buste restent libres.
					</p>
				</div>
			</div>
		</div>
	</div>
</section>

<style>
	.problem {
		padding: 7rem 2rem;
		position: relative;
		/* Subtle top border separates from ticker */
		border-top: 1px solid rgba(245, 240, 232, 0.05);
	}

	.problem-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 6rem;
		align-items: start;
	}

	/* ── Left column ── */
	.problem-left {
		position: sticky;
		top: 8rem; /* Sticks as user scrolls through the prose */
	}

	.problem-rule {
		width: 3rem;
		height: 2px;
		background: var(--amber);
		margin: 2rem 0;
	}

	.problem-pullquote {
		font-family: var(--f-serif);
		font-style: italic;
		font-size: 1.15rem;
		line-height: 1.6;
		color: var(--amber-pale);
		max-width: 28ch;
	}

	/* ── Right column — prose ── */
	.problem-body {
		font-family: var(--f-body);
		font-size: 1rem;
		line-height: 1.8;
		color: var(--paper-dim);
		margin-bottom: 1.5rem;
		max-width: 52ch;
	}

	/* The answer block — distinct from the problem paragraphs */
	.problem-answer {
		margin-top: 2.5rem;
		padding-top: 2.5rem;
		border-top: 1px solid rgba(245, 240, 232, 0.08);
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.answer-line {
		width: 2rem;
		height: 2px;
		background: var(--amber);
	}

	.answer-text {
		font-family: var(--f-body);
		font-size: 1rem;
		line-height: 1.8;
		color: var(--paper);
		max-width: 52ch;
	}

	/* ── Responsive ── */
	@media (max-width: 768px) {
		.problem-grid {
			grid-template-columns: 1fr;
			gap: 3rem;
		}

		.problem-left {
			position: static; /* No sticky on mobile */
		}

		.problem {
			padding: 5rem 1.25rem;
		}
	}
</style>
