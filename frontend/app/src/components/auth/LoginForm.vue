<template>
	<div class="row">
		<div class="col-md-6 offset-md-3 col-xl-4 offset-xl-4">
			<form>
				<div class="form-group">
					<label>Username</label>
					<input v-model="username" type="text" class="form-control" placeholder="Username">
				</div>
				<div class="form-group">
					<label>Email</label>
					<input v-model="email" type="email" class="form-control" placeholder="Email">
				</div>
                <div class="form-group">
					<label>Password</label>
					<input v-model="password" type="password" class="form-control" placeholder="Password">
				</div>
				<div class="form-group form-check">
					<input type="checkbox" class="form-check-input">
					<label class="form-check-label">Remember me</label>
				</div>
				<div v-if="invalidCredentials" class="form-group">
					<small class="text-danger">Invalid credentials</small>
				</div>
				<button type="submit" @click.prevent="register" class="btn btn-primary">Register</button>
			</form>
		</div>
	</div>
</template>
 

<script>
	import axios from 'axios'

	export default {
		data() {
			return {
				username: '',
				password: '',
                email: '',
				invalidCredentials: false,
			}
		},
		methods: {
		    register() {
		        let formData = {
                    username: this.username,
					password: this.password,
					email: this.email,
				}

				this.$store.dispatch('auth/login', formData).then(() => {
					this.$router.push('/dashboard');
				});
            },
			onSubmit() {
				let formData = {
					username: this.username,
					password: this.password,
				}

				this.$store.dispatch('auth/login', formData).then(() => {
					this.$router.push('/dashboard');
				});
			}
		}
	}
</script>
