<SEO {title} />

<h1>{title}</h1>

{#each works as work}
	<Work {work} />
{/each}

<script lang="ts">
	import SEO from '$lib/SEO.svelte'
	import works from './works'
	import Work from '$lib/work/Work.svelte'

	let title = 'Works'
</script>
