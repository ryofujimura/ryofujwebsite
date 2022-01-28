<h1>Contact</h1>

<form
	name="contact" method="post" action="/contact/success" data-netlify="true" netlify-honeypot="bot-field"
	bind:this={form} on:input={onInput}
>
	<input name="form-name" value="contact" type="hidden">
	<input name="bot-field" type="text" hidden>

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
</form>

<style>
	form {
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
</style>

<script lang="ts">
	$: form = null

	let valid: boolean = false

	function onInput() {
		valid = form.checkValidity()
	}
</script>

<script context="module" lang="ts">
	export const prerender = true
</script>
