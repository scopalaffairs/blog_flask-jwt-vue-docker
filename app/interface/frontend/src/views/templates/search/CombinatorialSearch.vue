<template>
    <div>
        <slot class="mb-5" name="set"></slot>

        <regulators-match class="mb-5" name="regulator_match_b">
            <template slot="label">
                <!--Set B that must match:-->
            </template>
        </regulators-match>

        <regulators-types class="mb-5" set="set B"></regulators-types>

        <filter-by-feature class="mb-5" name="filter_by_feature_b">
            <template slot="label">Look for binding sites in region:</template>
        </filter-by-feature>

    </div>
</template>

<script>
    import RegulatorsMatch from "./RegulatorsMatch";
    import RegulatorsTypes from "./RegulatorsTypes";
    import ButtonGroup from "../molecules/ButtonGroup";
    import PrimaryRadioButton from "../atoms/PrimaryRadioButton";
    import FilterByFeature from "./FilterByFeature";


    export default {
        name: "CombinatorialSearch",
        components: {
            FilterByFeature,
            RegulatorsTypes,
            RegulatorsMatch,
            ButtonGroup,
            PrimaryRadioButton
        },
        props: {
            'name': String
        }
    }
</script>

<style scoped>

</style>