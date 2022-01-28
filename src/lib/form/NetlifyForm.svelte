<form
	{name} {...$$props} method="post" data-netlify="true" netlify-honeypot="bot-field"
	bind:this={form} on:input={onInput}
>
	<input name="form-name" value={name} type="hidden">
	<input name="bot-field" type="text" hidden>

	<slot></slot>
</form>

<script lang="ts">
	export let name: string
	export let valid: boolean

	$: form = null

	function onInput() {
		valid = form.checkValidity()
	}
</script>
