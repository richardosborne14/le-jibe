<script lang="ts">
	/**
	 * Ticker — horizontal scrolling marquee strip between sections.
	 *
	 * Content describes brand positioning. Speed references and road context
	 * are explicitly excluded per positioning rules.
	 *
	 * Items are duplicated so the CSS animation loops seamlessly.
	 */

	const items = [
		'Conçu par un utilisateur',
		'Siège carbone sur mesure',
		'Rotation 360°',
		'Tout-terrain',
		'Fabriqué en France',
		'Roue stabilisatrice',
		'Joystick intuitif',
		'Production artisanale',
	];
</script>

<div class="ticker" aria-hidden="true">
	<div class="ticker-track">
		<!-- Duplicated twice for seamless infinite scroll illusion -->
		{#each [...items, ...items] as item, i}
			<span class="ticker-item">
				{item}
				<span class="ticker-dot"></span>
			</span>
		{/each}
	</div>
</div>

<style>
	.ticker {
		border-top: 1px solid rgba(245, 240, 232, 0.07);
		border-bottom: 1px solid rgba(245, 240, 232, 0.07);
		padding: 0.9rem 0;
		overflow: hidden;
		position: relative;
		background: var(--ink-soft);
	}

	.ticker-track {
		display: flex;
		gap: 0;
		white-space: nowrap;
		animation: ticker 35s linear infinite;
		/* Wide enough to hold all items before looping */
		width: max-content;
	}

	.ticker-item {
		display: inline-flex;
		align-items: center;
		gap: 1.5rem;
		padding: 0 2.5rem;
		font-family: var(--f-display);
		font-size: 0.72rem;
		font-weight: 600;
		letter-spacing: 0.15em;
		text-transform: uppercase;
		color: var(--muted);
	}

	.ticker-dot {
		width: 4px;
		height: 4px;
		border-radius: 50%;
		background: var(--amber);
		flex-shrink: 0;
	}

	@keyframes ticker {
		from { transform: translateX(0); }
		to   { transform: translateX(-50%); }
	}

	/* Pause on hover — accessibility and usability */
	.ticker:hover .ticker-track {
		animation-play-state: paused;
	}

	/* Respect prefers-reduced-motion */
	@media (prefers-reduced-motion: reduce) {
		.ticker-track {
			animation: none;
		}
	}
</style>
