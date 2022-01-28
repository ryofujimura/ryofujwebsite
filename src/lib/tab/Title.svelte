<a href={route.path} class="with-icon">
	<TextIcon/>
	{route.title}

	{#if route.subtitle}
		<span>{route.subtitle}</span>
	{/if}
</a>

<style>
	a {
		gap: 0.8ch;
		padding: 0.5ch;
		padding-left: 1ch;
	}

	a :global(svg) {
		width: 0.8em;
		height: 0.8em;
		opacity: 0.4;
	}

	span {
		opacity: 0.2;
		font-size: 0.8em;
	}
</style>

<script lang="ts">
	import TextIcon from '$lib/icon/Text.svelte'
	import routes from '$lib/routes'

	export let path: Path

	$: route = routes.find(route => route.path === path)
</script>
