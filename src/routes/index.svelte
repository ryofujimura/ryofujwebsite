<SEO />

<section>
	<Heading bind:offsetWidth>
		Ryo Fujimura — 💻 Software Developer
	</Heading>

	<div class="list">
		{#each featuredSkills as skill}
			<details>
				<summary style:--offset="{offsetWidth}px">
					{skill.name}
				</summary>

				<ul>
					{#each skill.works as work}
						<li>{work.title}</li>
					{/each}
				</ul>
			</details>
		{/each}
	</div>
</section>

<style>
	section {
		position: relative;
		display: grid;
		gap: 1rem;
	}

	.list {
		flex: 1 1;
	}

	@screen md {
		summary {
			margin-left: calc(var(--offset) + 1rem);
		}
	}

	ul {
		@apply bg-gray-50;
	}

	summary {
		display: inline-block;
	}

	summary::-webkit-details-marker {
		display: none;
	}
</style>

<script lang="ts">
	import SEO from '$lib/SEO.svelte'
	import Heading from '$lib/home/Heading.svelte'
	import { skillsWithWorks } from '$lib/skills'

	let offsetWidth: number

	let featuredSkills = skillsWithWorks
		.filter(({ featured, works }) => featured && works.length > 0)
</script>
