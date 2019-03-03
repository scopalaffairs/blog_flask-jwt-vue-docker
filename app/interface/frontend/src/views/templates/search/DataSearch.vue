<template>
    <div>
        <slot name="set"></slot>

        <set-operations></set-operations>

        <div class="flex justify-between">
            <div class="text-grey-darker text-center pt-2">
                <secondary-button>
                    Clear
                </secondary-button>
            </div>
            <div class="text-grey-darker text-center pt-2">
                <primary-button type="submit">
                    Search
                </primary-button>
            </div>
        </div>

    </div>
</template>

<script>
    import PrimaryRadioButton from "../atoms/PrimaryRadioButton";
    import FilterByFeature from "./FilterByFeature";
    import TagsInput from "./TagsInput";
    import SetOperations from "./SetOperations";
    import TriggerData from "./TriggerData";
    import SecondaryButton from "../atoms/SecondaryButton";
    import PrimaryButton from "../atoms/PrimaryButton";


    export default {
        name: "CombinatorialSearch",
        components: {
            PrimaryButton,
            SecondaryButton,
            TriggerData,
            SetOperations,
            TagsInput,
            FilterByFeature,
            PrimaryRadioButton
        },
        props: {
            'value': String,
            'name': String
        }
    }
</script>

<style scoped>

</style>