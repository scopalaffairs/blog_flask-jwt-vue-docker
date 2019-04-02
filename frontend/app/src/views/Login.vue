<template>
    <div>
        <h2>Login</h2>
        <form>
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" class="form-control"/>
            </div>
            <div class="form-group">
                <label>Password</label>
                <input type="password" class="form-control"/>
            </div>
            <div class="form-group">
                <button class="btn btn-primary">Login</button>
            </div>
        </form>
    </div>
</template>

<script>
    export default {
        name: 'Login',
        data() {
            return {}
        }
    };
</script>
