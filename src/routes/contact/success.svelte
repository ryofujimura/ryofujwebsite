<SEO {title} />

<h1 class="h1">{title}</h1>

<p>I'll be in contact shortly!</p>

<script lang="ts">
	import SEO from '$lib/SEO.svelte'

	let title = 'Thanks for your submission!'
</script>

<script context="module" lang="ts">
	export const prerender = true
</script>
