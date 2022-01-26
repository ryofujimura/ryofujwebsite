<svelte:head>
	{#if title}
		<title>{title} | {site.title}</title>
	{:else}
		<title>{site.title}</title>
	{/if}

	<meta name="description" content={description || site.description}>
</svelte:head>

<script lang="ts">
	import site from './site'

	export let title: string | undefined = undefined
	export let description: string | undefined = undefined
</script>
