<template>

        <div class="container">
            <br>
            <br>

            <div class="row align-items-center justify-content-center">
                <h1>Add a book</h1>
            </div>
            <br>

            <form method="POST">

                <label for="name">Book Name</label>
                <div class="form-row">
                    <input class="form-control" type="text" placeholder="Name of Book" id="name" name="name">
                </div>
                <br>
                <div class="form-row">
                    <label for="author">Author</label>
                    <input class="form-control" type="text" placeholder="Author Name" id="author" name="author">
                </div>
                <br>
                <div class="form-row ">
                    <label for="published">Published</label>
                    <input class="form-control " type="date" placeholder="Published" id="published" name="published">
                </div>

                <br>
                <button type="submit " class="btn btn-primary " style="float:right ">Submit</button>

            </form>
            <br><br>
        </div>
</template>

<script>
    export default {
        name: "books"
    }
</script>

<style scoped>

</style>
