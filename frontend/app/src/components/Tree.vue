<template>
    <tree :data="tree" :node-text="name" layoutType="circular">
    </tree>
</template>
<script>
    import {tree} from 'vued3tree'

    export default {
        components: {
            tree
        },
        data() {
            return {
                tree: {
                    name: "father",
                    children: [{
                        name: "son1",
                        children: [{name: "grandson"}, {name: "grandson2"}]
                    }, {
                        name: "son2",
                        children: [{name: "grandson3"}, {name: "grandson4"}]
                    }]
                }
            }
        }
    }
</script>

<style>
    .treeclass .nodetree circle {
        fill: #999;
    }

    .treeclass .node--internal circle {
        cursor: pointer;
        fill: #555;
    }

    .treeclass .nodetree text {
        font: 10px sans-serif;
        cursor: pointer;
    }

    .treeclass .nodetree.selected text {
        font-weight: bold;
    }

    .treeclass .node--internal text {
        text-shadow: 0 1px 0 #fff, 0 -1px 0 #fff, 1px 0 0 #fff, -1px 0 0 #fff;
    }

    .treeclass .linktree {
        fill: none;
        stroke: #555;
        stroke-opacity: 0.4;
        stroke-width: 1.5px;
    }
</style>
