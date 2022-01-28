<SEO title={work.title} />

<h1 class="h1">{work.title}</h1>

<ul class="skills">
	{#each work.skills as skill}
		<li>{skill}</li>
	{/each}
</ul>

<style>
	.skills {
		list-style: disc;
		margin-left: 2em;
	}
</style>

<script lang="ts">
	import SEO from '$lib/SEO.svelte'

	export let work: Work
</script>

<script context="module" lang="ts">
	import works from '$lib/works'

	export async function load({ params }) {
		const work = works.find(work => params.id === work.id)

		if (!!work) {
			return {
				props: {
					work
				}
			}
		}

		return {
			status: 404
		}
	}
</script>
