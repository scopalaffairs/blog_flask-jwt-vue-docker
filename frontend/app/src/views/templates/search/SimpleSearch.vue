<template>
    <div>
        <slot name="set"></slot>

        <regulators-match class="mb-5" name="regulator_match_a">
            <template slot="label">
                <!--Set A:-->
            </template>
        </regulators-match>

        <regulators-types class="mb-5" set="set A"></regulators-types>

        <filter-by-feature class="mb-5" name="filter_by_feature_a">
            <template slot="label">Filter by feature:</template>
        </filter-by-feature>

        <limit-targets class="mb-5"></limit-targets>

    </div>
</template>

<script>
    import LimitTargets from "./LimitTargets";
    import RegulatorsTypes from "./RegulatorsTypes";
    import RegulatorsMatch from "./RegulatorsMatch";
    import FilterByFeature from "./FilterByFeature";

    export default {
        name: "SimpleSearch",
        components: {
            LimitTargets,
            RegulatorsTypes,
            RegulatorsMatch,
            FilterByFeature
        },
        props: {
            'name': String
        }
    }
</script>

<style scoped>

</style>