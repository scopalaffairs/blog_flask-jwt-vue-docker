<template>
    <div class="btn-pill mt-1">
        <label class="btn-pill--wrapper">
            <input type="radio"
                   :name="name"
                   :value="value">
            <span class="checkmark"></span>
            <slot></slot>
        </label>
    </div>
</template>

<script>
    export default {
        name: "PrimaryRadioButtonPillBar",
        props: ['value', 'name']
    }
</script>

<style scoped>

    .btn-pill {

        cursor: pointer;
        border-radius: 0.125rem;
        border-top: #006699 1px solid;
        border-bottom: #006699 1px solid;
        border-right: #006699 1px solid;
        border-left: #006699 1px solid;
        background-color: white;
        line-height: 28px;
        text-align: center;
        color: #006699;
        display: inline-flex;
        margin-right: 3px;
        font-size: smaller;
    }

    .btn-pill .btn-pill--wrapper {
        position: relative;
        cursor: pointer;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        padding: 0 5px 0 5px;
    }

    .btn-pill .btn-pill--wrapper input {
        display: none;
    }

    .btn-pill input .checkmark {
        background-color: #eee;
    }

    .btn-pill .btn-pill--wrapper:hover input ~ .checkmark {
        background-color: #ccc;
    }

    .btn-pill .btn-pill--wrapper input:checked ~ .checkmark {
        background-color: #2196F3;
    }

    .btn-pill .checkmark:after {
        content: "";
        position: absolute;
        display: none;
    }

    .btn-pill .btn-pill--wrapper input:checked ~ .checkmark:after {
        display: block;
    }

    .btn-pill .btn-pill--wrapper .checkmark:after {
        position: absolute;
        left: 0;
        width: 100%;
        height: 100%;
        opacity: .3;
        background-color: #6cb2eb;
    }

</style>