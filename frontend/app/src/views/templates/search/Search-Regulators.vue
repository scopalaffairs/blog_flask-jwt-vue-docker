<template>
    <accordion-list>
        <accordion-item :item-id="1">
            <template slot="header">
                Regulators
            </template>
            <template slot="content">
                <simple-search>
                    <template slot="set">Choose set A</template>
                </simple-search>
            </template>
        </accordion-item>
        <accordion-item :item-id="2">
            <template slot="header">
                Combinatorial Search
            </template>
            <template slot="content">
                <combinatorial-search>
                    <template slot="set">Choose set B</template>
                </combinatorial-search>
            </template>
        </accordion-item>
        <accordion-item :item-id="3">
            <template slot="header">
                Set Operations
            </template>
            <template slot="content">
                <data-search>
                    <template slot="set">Filter datasets</template>
                </data-search>
            </template>
        </accordion-item>
    </accordion-list>
</template>

<script>

    import PrimaryButton from "../atoms/PrimaryButton.vue"
    import SecondaryButton from "../atoms/SecondaryButton.vue"
    import AccordionList from "../../../components/AccordionList.vue"
    import AccordionItem from "../../../components/AccordionItem.vue"

    import TagsInput from "./TagsInput.vue"
    import FilterByFeature from "./FilterByFeature";
    import SetOperations from "./SetOperations";
    import RegulatorsMatch from "./RegulatorsMatch";
    import CombinatorialSearch from "./CombinatorialSearch";
    import TriggerData from "./TriggerData";
    import LimitTargets from "./LimitTargets";
    import RegulatorsTypes from "./RegulatorsTypes";
    import SimpleSearch from "./SimpleSearch";
    import DataSearch from "./DataSearch";

    export default {
        components: {
            SimpleSearch,
            RegulatorsTypes,
            LimitTargets,
            PrimaryButton,
            SecondaryButton,
            TriggerData,
            CombinatorialSearch,
            RegulatorsMatch,
            SetOperations,
            FilterByFeature,
            AccordionList,
            AccordionItem,
            TagsInput,
            DataSearch
        },
        data() {
            return {}
        }
    }
</script>
