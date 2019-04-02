<template>
        <div class="container">
            <div class="row align-items-center justify-content-center">
                <h1>Add a book</h1>
            </div>
            <form method="POST">
                <label for="name">Book Name</label>
                <div class="form-row">
                    <input class="form-control" type="text" placeholder="Name of Book" id="name" name="name">
                </div>
                <div class="form-row">
                    <label for="author">Author</label>
                    <input class="form-control" type="text" placeholder="Author Name" id="author" name="author">
                </div>
                <div class="form-row">
                    <label for="published">Published</label>
                    <input class="" type="date" placeholder="Published" id="published" name="published">
                </div>

                <button type="submit" class="">Submit</button>
            </form>
        </div>
</template>

<script>
    export default {
        name: "books"
    }
</script>

<style scoped>

</style>
