<ul class="bg-gray-100">
	{#each works as work}
		<li>{work.title}</li>
	{/each}
</ul>

<style>
	ul {
		margin-left: -2rem;
		width: calc(100% + 4rem);
		padding: 1rem 2rem;
		margin-block: 1rem;
	}

	@screen <md {
		ul {
			width: 100vw;
			margin-inline: calc(50% - 50vw);
		}
	}
</style>

<script lang="ts">
	export let works: Work[]
</script>
