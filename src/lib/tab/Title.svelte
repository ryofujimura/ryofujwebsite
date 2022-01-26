<a href={route.path} class="with-icon">
	<TextIcon/>
	{route.title}
</a>

<style>
	a {
		padding: 0.5ch;
		padding-left: 1ch;
	}

	a :global(svg) {
		width: 0.8em;
		height: 0.8em;
		opacity: 0.4;
	}
</style>

<script lang="ts">
	import TextIcon from '$lib/icon/Text.svelte'
	import routes from '$lib/routes'

	export let path: Path

	$: route = routes.find(route => route.path === path)
</script>
