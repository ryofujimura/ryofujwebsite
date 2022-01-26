<svelte:head>
	<title>{work.title}</title>
</svelte:head>

<h1>{work.title}</h1>

<script lang="ts">
	export let work: Work
</script>

<script context="module" lang="ts">
	import works from './works'

	export async function load({ params }) {
		let work = works.find(({ id }) => id === params.id)

		if (!!work) {
			return {
				props: {
					work,
				}
			}
		}

		return {
			status: 404,
		}
	}
</script>
