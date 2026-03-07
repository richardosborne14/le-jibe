<script lang="ts">
	/**
	 * Edit post page — /admin/posts/[id]/edit
	 *
	 * Pre-fills form with existing post data loaded via +page.ts.
	 * Same editor/preview layout as the new post form.
	 *
	 * Additional action: "Dépublier" (unpublish) if currently published.
	 */
	import { goto } from '$app/navigation';
	import { untrack } from 'svelte';
	import { marked } from 'marked';
	import DOMPurify from 'dompurify';

	let { data } = $props();
	// $derived keeps post reactive if data is updated (e.g. invalidation)
	const post = $derived(data.post);

	// untrack() signals to Svelte that reading data here is intentionally one-shot:
	// title and bodyMd are independently editable form state, not derived from data.
	let title = $state(untrack(() => data.post?.title ?? ''));
	let bodyMd = $state(untrack(() => data.post?.body_md ?? ''));
	let saving = $state(false);
	let saveError = $state('');

	/** Reactive preview — updates in real time as user types. */
	let previewHtml = $derived(
		bodyMd
			? DOMPurify.sanitize(marked.parse(bodyMd) as string)
			: '<p style="color: var(--muted); font-style: italic;">Aperçu du contenu…</p>'
	);

	function getToken(): string | null {
		const token = sessionStorage.getItem('admin_token');
		if (!token) goto('/admin');
		return token;
	}

	/**
	 * Patch the post with given fields.
	 * publish=true → publish, publish=false → unpublish, publish=null → keep current.
	 */
	async function save(publish: boolean | null) {
		if (!title.trim()) { saveError = 'Le titre est obligatoire.'; return; }
		if (!bodyMd.trim()) { saveError = 'Le contenu est obligatoire.'; return; }

		const token = getToken();
		if (!token) return;

		saving = true;
		saveError = '';

		const payload: Record<string, unknown> = {
			title: title.trim(),
			body_md: bodyMd,
		};

		// Only set published if the caller explicitly changed it
		if (publish !== null) {
			payload.published = publish;
		}

		try {
			const res = await fetch(`/api/admin/posts/${post.id}`, {
				method: 'PATCH',
				headers: {
					'Content-Type': 'application/json',
					Authorization: `Bearer ${token}`,
				},
				body: JSON.stringify(payload),
			});

			if (res.status === 401 || res.status === 403) {
				sessionStorage.removeItem('admin_token');
				goto('/admin');
				return;
			}

			if (!res.ok) {
				const err = await res.json().catch(() => ({}));
				saveError = err.detail ?? `Erreur ${res.status}.`;
				return;
			}

			goto('/admin/posts');
		} catch {
			saveError = 'Impossible de joindre le serveur.';
		} finally {
			saving = false;
		}
	}

	function handleLogout() {
		sessionStorage.removeItem('admin_token');
		goto('/admin');
	}
</script>

<svelte:head>
	<title>Modifier — {post?.title ?? 'Article'} — Admin Le Jibé</title>
</svelte:head>

<div class="admin-page">
	<header class="admin-nav">
		<a href="/" class="admin-logo">Le <span>Jibé</span></a>
		<nav class="admin-links">
			<a href="/admin/signups" class="admin-link">Inscriptions</a>
			<a href="/admin/posts" class="admin-link active">Articles</a>
		</nav>
		<button class="btn-logout" onclick={handleLogout}>Déconnexion</button>
	</header>

	<main class="admin-main">
		<div class="page-header">
			<div>
				<a href="/admin/posts" class="back-link">← Articles</a>
				<h1 class="page-title">Modifier l'article</h1>
				<p class="post-status">
					{post?.published ? '● Publié' : '○ Brouillon'}
				</p>
			</div>
			<div class="action-group">
				{#if saveError}
					<span class="save-error" role="alert">{saveError}</span>
				{/if}

				<!-- Unpublish — only shown if currently published -->
				{#if post?.published}
					<button class="btn-unpublish" onclick={() => save(false)} disabled={saving}>
						Dépublier
					</button>
				{/if}

				<!-- Save as draft — keep current published state -->
				<button class="btn-draft" onclick={() => save(null)} disabled={saving}>
					{saving ? 'Enregistrement…' : 'Enregistrer'}
				</button>

				<!-- Publish — always available -->
				<button class="btn-publish" onclick={() => save(true)} disabled={saving}>
					{post?.published ? 'Mettre à jour →' : 'Publier →'}
				</button>
			</div>
		</div>

		<div class="title-field">
			<input
				class="title-input"
				type="text"
				placeholder="Titre de l'article"
				bind:value={title}
				disabled={saving}
			/>
		</div>

		<div class="editor-layout">
			<div class="editor-pane">
				<div class="pane-label">Markdown</div>
				<textarea
					class="form-textarea editor-textarea"
					placeholder="Contenu en Markdown…"
					bind:value={bodyMd}
					disabled={saving}
				></textarea>
			</div>

			<div class="preview-pane">
				<div class="pane-label">Aperçu</div>
				<div class="prose preview-body">
					<!-- eslint-disable-next-line svelte/no-at-html-tags -->
					{@html previewHtml}
				</div>
			</div>
		</div>
	</main>
</div>

<style>
	.admin-page {
		min-height: 100vh;
		background: var(--ink);
		display: flex;
		flex-direction: column;
	}

	.admin-nav {
		display: flex;
		align-items: center;
		gap: 2rem;
		padding: 1rem 2rem;
		background: var(--ink-soft);
		border-bottom: 1px solid rgba(245, 240, 232, 0.07);
		position: sticky;
		top: 0;
		z-index: 10;
	}

	.admin-logo {
		font-family: var(--f-display);
		font-weight: 800;
		font-size: 1rem;
		color: var(--white);
		letter-spacing: 0.05em;
		margin-right: auto;
	}

	.admin-logo span { color: var(--amber); }
	.admin-links { display: flex; gap: 1.5rem; }

	.admin-link {
		font-family: var(--f-display);
		font-size: 0.75rem;
		font-weight: 600;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: var(--muted);
		transition: color 0.2s;
		padding-bottom: 2px;
	}

	.admin-link:hover, .admin-link.active {
		color: var(--amber-bright);
		border-bottom: 1px solid var(--amber);
	}

	.btn-logout {
		font-family: var(--f-display);
		font-size: 0.7rem;
		font-weight: 600;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: var(--muted);
		background: none;
		border: 1px solid rgba(245, 240, 232, 0.12);
		border-radius: 2px;
		padding: 0.35rem 0.75rem;
		cursor: pointer;
	}

	.admin-main {
		padding: 2rem;
		flex: 1;
		display: flex;
		flex-direction: column;
	}

	.page-header {
		display: flex;
		align-items: flex-start;
		justify-content: space-between;
		margin-bottom: 1.5rem;
		gap: 1rem;
	}

	.back-link {
		font-size: 0.75rem;
		color: var(--muted);
		font-family: var(--f-display);
		letter-spacing: 0.06em;
		display: block;
		margin-bottom: 0.25rem;
		transition: color 0.2s;
	}

	.back-link:hover { color: var(--paper); }

	.page-title {
		font-family: var(--f-display);
		font-weight: 700;
		font-size: 1.4rem;
		color: var(--white);
	}

	.post-status {
		font-size: 0.68rem;
		font-family: var(--f-display);
		font-weight: 600;
		color: var(--amber);
		letter-spacing: 0.08em;
		text-transform: uppercase;
		margin-top: 0.2rem;
	}

	.action-group {
		display: flex;
		align-items: center;
		gap: 0.75rem;
		flex-wrap: wrap;
		justify-content: flex-end;
	}

	.save-error {
		font-size: 0.78rem;
		color: #e05252;
	}

	.btn-unpublish {
		font-family: var(--f-display);
		font-size: 0.72rem;
		font-weight: 600;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		padding: 0.6rem 1rem;
		background: transparent;
		color: #e05252;
		border: 1px solid rgba(224, 82, 82, 0.3);
		border-radius: 2px;
		cursor: pointer;
		transition: background 0.2s;
	}

	.btn-unpublish:hover:not(:disabled) { background: rgba(224, 82, 82, 0.08); }
	.btn-unpublish:disabled { opacity: 0.4; cursor: not-allowed; }

	.btn-draft {
		font-family: var(--f-display);
		font-size: 0.75rem;
		font-weight: 600;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		padding: 0.6rem 1.25rem;
		background: transparent;
		color: var(--muted);
		border: 1px solid rgba(245, 240, 232, 0.12);
		border-radius: 2px;
		cursor: pointer;
		transition: color 0.2s;
	}

	.btn-draft:hover:not(:disabled) { color: var(--paper); }
	.btn-draft:disabled { opacity: 0.5; cursor: not-allowed; }

	.btn-publish {
		font-family: var(--f-display);
		font-size: 0.75rem;
		font-weight: 700;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		padding: 0.6rem 1.25rem;
		background: var(--amber);
		color: var(--ink);
		border: none;
		border-radius: 2px;
		cursor: pointer;
		transition: background 0.2s;
	}

	.btn-publish:hover:not(:disabled) { background: var(--amber-bright); }
	.btn-publish:disabled { opacity: 0.5; cursor: not-allowed; }

	.title-field { margin-bottom: 1.5rem; }

	.title-input {
		width: 100%;
		background: transparent;
		border: none;
		border-bottom: 1px solid rgba(245, 240, 232, 0.12);
		color: var(--white);
		font-family: var(--f-display);
		font-weight: 700;
		font-size: clamp(1.4rem, 3vw, 2rem);
		padding: 0.5rem 0;
		outline: none;
		transition: border-color 0.2s;
	}

	.title-input::placeholder { color: rgba(138, 133, 120, 0.4); }
	.title-input:focus { border-color: var(--amber); }

	.editor-layout {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 1.5rem;
		flex: 1;
		min-height: 500px;
	}

	.editor-pane, .preview-pane {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
	}

	.pane-label {
		font-family: var(--f-display);
		font-size: 0.65rem;
		font-weight: 700;
		letter-spacing: 0.2em;
		text-transform: uppercase;
		color: var(--muted);
	}

	.editor-textarea {
		flex: 1;
		min-height: 480px;
		font-family: 'Courier New', monospace;
		font-size: 0.85rem;
		line-height: 1.6;
		resize: none;
	}

	.preview-pane {
		border: 1px solid rgba(245, 240, 232, 0.07);
		border-radius: 2px;
	}

	.preview-body {
		flex: 1;
		padding: 1.25rem;
		overflow-y: auto;
		max-width: none;
	}

	@media (max-width: 900px) {
		.editor-layout { grid-template-columns: 1fr; }
		.preview-pane { min-height: 300px; }
	}
</style>
