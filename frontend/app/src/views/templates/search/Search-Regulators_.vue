<template>
    <div>
        <div class="flex">
            <div class="w-full md:w-1/2 xl:flex-1 lg:flex-1 md:flex-1 sm:flex-0 xs:flex-0  shadow-lg text-grey-darker px-4 py-2 m-2">
                <tags-input class=""></tags-input>
            </div>
        </div>
        <div class="flex flex-wrap">
            <div class="sm:w-full md:w-1/2 xl:flex-1 lg:flex-1 md:flex-1 sm:flex-0 xs:flex-0 shadow-lg text-grey-darker px-4 py-2 m-2">
                <h3 class="pt-3 pb-3">Regulators</h3>

                <simple-search class="p-8 pb-3">
                    <template slot="set">Choose set A</template>
                </simple-search>
            </div>
            <div class="sm:w-full md:w-1/2 xl:flex-1 lg:flex-1 md:flex-1 sm:flex-0 xs:flex-0 shadow-lg text-grey-darker px-4 py-2 m-2">
                <h3 class="pt-3 pb-3">Combinatorial Search</h3>

                <combinatorial-search class="p-8 pb-3">
                    <template slot="set">Choose set B</template>
                </combinatorial-search>
            </div>


        </div>
        <div class="flex-0 shadow-lg text-grey-darker px-4 py-2 m-2">
                    <h3 class="pt-3 pb-3">Set Operations</h3>
            <data-search class="p-8 pb-3">
                <template slot="set">
                </template>
            </data-search>
        </div>
    </div>
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
