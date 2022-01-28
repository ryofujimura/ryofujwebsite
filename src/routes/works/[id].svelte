<h1 class="h1">{work.title}</h1>

<script lang="ts">
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
