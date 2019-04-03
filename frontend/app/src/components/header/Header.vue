<template>
	<div toggleable type="light" variant="light" class="mb-5">
		<div target="nav_text_collapse"></div>
		<div>Analytics</div>

		<div is-nav id="nav_text_collapse">
			<div>
				<div>
					<router-link to="/" class="nav-link">Home</router-link>
				</div>
				<div v-if="!isAuth">
					<router-link to="/login" class="nav-link">Login</router-link>
				</div>
				<div v-if="isAuth">
					<router-link to="/dashboard" class="nav-link">Dashboard</router-link>
				</div>
			</div>

			<div v-if="isAuth" class="ml-auto">
				<div text="" right>
					<div href="#">Account</div>
					<div href="#" @click="onLogout">Logout</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import { mapGetters } from 'vuex'

	export default {
		computed: {
			...mapGetters('auth', {
				isAuth: 'isAuthenticated',
			})
		}
	}
</script>
