<script lang="ts">
	/**
	 * SignupForm — interest registration form (Task 5).
	 *
	 * Three states:
	 *  - idle: form visible, submit enabled
	 *  - loading: inputs disabled, button shows spinner
	 *  - success: form replaced by confirmation message (no page reload)
	 *
	 * API: POST /api/signups (proxied through nginx)
	 * Error handling:
	 *  - 409 → "Cet email est déjà inscrit."
	 *  - Other → generic French message
	 *
	 * Profile type values sent to API are English enums.
	 * Display labels are French — mapping defined in profileOptions.
	 *
	 * Note: variable named `formState` (not `state`) to avoid conflicting
	 * with the Svelte 5 `$state` rune identifier.
	 */

	type FormState = 'idle' | 'loading' | 'success';

	let formState: FormState = $state('idle');
	let errorMessage: string = $state('');

	// Form field values
	let firstName = $state('');
	let email = $state('');
	let profileType = $state('');

	// Validation errors per field — shown inline on submit attempt
	let fieldErrors: Record<string, string> = $state({});

	/** French label → English enum value sent to the API. */
	const profileOptions: Array<{ label: string; value: string }> = [
		{ label: 'Utilisateur de fauteuil roulant', value: 'user' },
		{ label: "Aidant ou proche d'un utilisateur", value: 'caregiver' },
		{ label: 'Professionnel de santé / ergothérapeute', value: 'professional' },
		{ label: 'Autre', value: 'other' },
	];

	/** Client-side validation before hitting the API. Returns true if valid. */
	function validate(): boolean {
		const errors: Record<string, string> = {};

		if (!firstName.trim()) {
			errors.firstName = 'Prénom requis.';
		}

		if (!email.trim()) {
			errors.email = 'Email requis.';
		} else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
			errors.email = "Format d'email invalide.";
		}

		if (!profileType) {
			errors.profileType = 'Veuillez choisir un profil.';
		}

		fieldErrors = errors;
		return Object.keys(errors).length === 0;
	}

	/** Submit handler — validates then calls the API. */
	async function handleSubmit(event: SubmitEvent) {
		event.preventDefault();
		errorMessage = '';

		if (!validate()) return;

		formState = 'loading';

		try {
			const response = await fetch('/api/signups', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({
					first_name: firstName.trim(),
					email: email.trim().toLowerCase(),
					profile_type: profileType,
				}),
			});

			if (response.ok) {
				formState = 'success';
				return;
			}

			// Handle known error cases explicitly
			if (response.status === 409) {
				errorMessage = 'Cet email est déjà inscrit.';
			} else {
				errorMessage = 'Une erreur est survenue. Veuillez réessayer dans quelques instants.';
			}

			formState = 'idle';
		} catch {
			// Network error — no silent failures
			errorMessage = 'Impossible de contacter le serveur. Vérifiez votre connexion.';
			formState = 'idle';
		}
	}
</script>

{#if formState === 'success'}
	<!-- Success state — replaces form, no page reload -->
	<div class="signup-success" role="status" aria-live="polite">
		<div class="success-icon" aria-hidden="true">✓</div>
		<h3 class="success-title">Merci, {firstName} !</h3>
		<p class="success-message">
			Nous vous tiendrons informé(e) dès que Le Jibé sera disponible à la précommande. Restez à
			l'écoute.
		</p>
		<p class="success-sub">Inscrit(e) avec {email}</p>
	</div>
{:else}
	<!-- Signup form — idle and loading states share the same markup -->
	<form class="signup-form" onsubmit={handleSubmit} novalidate>
		<div class="form-row">
			<div class="form-group">
				<label class="form-label" for="signup-fname">Prénom</label>
				<input
					class="form-input"
					class:error={fieldErrors.firstName}
					id="signup-fname"
					type="text"
					placeholder="Jean"
					bind:value={firstName}
					disabled={formState === 'loading'}
					autocomplete="given-name"
					required
				/>
				{#if fieldErrors.firstName}
					<span class="field-error" role="alert">{fieldErrors.firstName}</span>
				{/if}
			</div>

			<div class="form-group">
				<label class="form-label" for="signup-email">Email</label>
				<input
					class="form-input"
					class:error={fieldErrors.email}
					id="signup-email"
					type="email"
					placeholder="jean@exemple.fr"
					bind:value={email}
					disabled={formState === 'loading'}
					autocomplete="email"
					required
				/>
				{#if fieldErrors.email}
					<span class="field-error" role="alert">{fieldErrors.email}</span>
				{/if}
			</div>
		</div>

		<div class="form-group">
			<label class="form-label" for="signup-profile">Vous êtes…</label>
			<select
				class="form-select"
				class:error={fieldErrors.profileType}
				id="signup-profile"
				bind:value={profileType}
				disabled={formState === 'loading'}
				required
			>
				<option value="" disabled>Choisissez votre profil</option>
				{#each profileOptions as opt}
					<option value={opt.value}>{opt.label}</option>
				{/each}
			</select>
			{#if fieldErrors.profileType}
				<span class="field-error" role="alert">{fieldErrors.profileType}</span>
			{/if}
		</div>

		<!-- Global API error message -->
		{#if errorMessage}
			<div class="form-error" role="alert">{errorMessage}</div>
		{/if}

		<button
			type="submit"
			class="btn-submit"
			disabled={formState === 'loading'}
			aria-busy={formState === 'loading'}
		>
			{#if formState === 'loading'}
				<span class="spinner" aria-hidden="true"></span>
				En cours…
			{:else}
				Manifester son intérêt →
			{/if}
		</button>

		<p class="form-note">
			Aucun engagement. Désinscription possible à tout moment. Données stockées en UE.
		</p>
	</form>
{/if}

<style>
	/* ── Form layout ── */
	.signup-form {
		display: flex;
		flex-direction: column;
		gap: 1rem;
		width: 100%;
	}

	.form-row {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 1rem;
	}

	.form-group {
		display: flex;
		flex-direction: column;
		gap: 0.4rem;
	}

	/* Input error highlight — uses :global because class is toggled dynamically */
	:global(.form-input.error),
	:global(.form-select.error) {
		border-color: #e05252;
	}

	.field-error {
		font-size: 0.72rem;
		color: #e05252;
		margin-top: 0.1rem;
	}

	.form-error {
		background: rgba(224, 82, 82, 0.08);
		border: 1px solid rgba(224, 82, 82, 0.3);
		border-radius: 2px;
		padding: 0.75rem 1rem;
		font-size: 0.85rem;
		color: #e05252;
	}

	/* ── Submit button ── */
	.btn-submit {
		font-family: var(--f-display);
		font-weight: 700;
		font-size: 0.82rem;
		letter-spacing: 0.14em;
		text-transform: uppercase;
		padding: 1.1rem 2.5rem;
		background: var(--amber);
		color: var(--ink);
		border: none;
		border-radius: 2px;
		cursor: pointer;
		transition:
			background 0.2s,
			transform 0.15s,
			opacity 0.2s;
		align-self: center;
		margin-top: 0.5rem;
		display: flex;
		align-items: center;
		gap: 0.5rem;
	}

	.btn-submit:hover:not(:disabled) {
		background: var(--amber-bright);
		transform: translateY(-1px);
	}

	.btn-submit:disabled {
		opacity: 0.7;
		cursor: not-allowed;
		transform: none;
	}

	/* CSS spinner for loading state — no image dependency */
	.spinner {
		width: 14px;
		height: 14px;
		border: 2px solid rgba(13, 13, 11, 0.3);
		border-top-color: var(--ink);
		border-radius: 50%;
		animation: spin 0.6s linear infinite;
		flex-shrink: 0;
	}

	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
	}

	.form-note {
		font-size: 0.72rem;
		color: rgba(138, 133, 120, 0.7);
		text-align: center;
		margin-top: 0.25rem;
	}

	/* ── Success state ── */
	.signup-success {
		text-align: center;
		padding: 2rem;
	}

	.success-icon {
		font-size: 2rem;
		color: var(--amber);
		margin-bottom: 1rem;
	}

	.success-title {
		font-family: var(--f-display);
		font-weight: 700;
		font-size: 1.4rem;
		color: var(--white);
		margin-bottom: 0.75rem;
	}

	.success-message {
		font-size: 0.95rem;
		color: var(--paper-dim);
		line-height: 1.6;
		max-width: 40ch;
		margin: 0 auto 0.75rem;
	}

	.success-sub {
		font-size: 0.75rem;
		color: var(--muted);
	}

	/* ── Responsive ── */
	@media (max-width: 640px) {
		.form-row {
			grid-template-columns: 1fr;
		}
	}
</style>
