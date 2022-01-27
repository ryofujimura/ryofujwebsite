<div class:md:hidden={!offsetWidth}>
	<div class="offset" style:--offset="{offsetWidth}px">
		💻 Software Developer
	</div>

	{#each featuredSkills as skill}
		<details open={$activeFeaturedSkill === skill.name}>
			<summary
				class="offset"
				style:--offset="{offsetWidth}px"
				on:click|preventDefault={() => onClick(skill.name)}
			>
				{skill.name}
			</summary>

			<ul class="bg-gray-50">
				{#each skill.works as work}
					<li>{work.title}</li>
				{/each}
			</ul>
		</details>
	{/each}
</div>

<style>
	@screen md {
		.offset {
			margin-left: calc(var(--offset) + 1rem);
		}
	}

	summary {
		display: inline-block;
	}

	summary::-webkit-details-marker {
		display: none;
	}
</style>

<script lang="ts">
	import { skillsWithWorks } from '$lib/skills'
	import { activeFeaturedSkill, localStore } from '$lib/store'

	export let offsetWidth: number

	let featuredSkills = skillsWithWorks
		.filter(({ featured, works }) => featured && works.length > 0)

	function onClick(name: string) {
		if ($activeFeaturedSkill === name) {
			$activeFeaturedSkill = null
		} else {
			$activeFeaturedSkill = name
		}

		localStore('activeFeaturedSkill', $activeFeaturedSkill)
	}
</script>
