<SEO {title} />

<section>
	<h1 class="h1">{title}</h1>

	<NetlifyForm name="contact" action="/contact/success" {valid}>
		<label>
			<span>Name:</span>
			<input class="input" name="name" type="text" autocomplete="name" placeholder="Name" required>
		</label>

		<label>
			<span>Email:</span>
			<input class="input" name="email" type="email" autocomplete="email" placeholder="Email" required>
		</label>

		<label>
			<span>Message:</span>
			<textarea class="input" name="message" placeholder="Message" required></textarea>
		</label>

		<button class="button" disabled={!valid}>Submit</button>
	</NetlifyForm>
</section>

<style>
	section :global(form) {
		display: grid;
		gap: 0.5rem;
	}

	label {
		display: grid;
	}

	@screen md {
		label {
			grid-template-columns: 8em 1fr;
		}
	}

	span {
		padding: 0.5ch 0;
	}

	button {
		margin-top: 1rem;
	}
</style>

<script lang="ts">
	import SEO from '$lib/SEO.svelte'
	import NetlifyForm from '$lib/form/NetlifyForm.svelte'

	let title = 'Contact'

	let valid: boolean = false
</script>

<script context="module" lang="ts">
	export const prerender = true
</script>
