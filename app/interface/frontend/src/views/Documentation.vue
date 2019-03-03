<template>
    <div>
        <card>
            <template slot="heading">
                API documentation
            </template>
            <template slot="text-body" class="text-sm">
                <ul class="" id="pills-tab" role="tablist">
                    <li class="nav-item">
                        <a class="nav-link"
                           id="rest-api-tab"
                           href="#rest-api"
                        >Rest API</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link"
                           id="python-api-tab"
                           href="#python-api"
                        >Python API</a>
                    </li>
                </ul>
            </template>
            <template slot="tags">
            </template>
        </card>

        <card>
            <template slot="heading">
                Python API
            </template>
            <template slot="text-body" class="text-sm">
                The dorina python API can be used to run local dorina queries. The
                central entry point for all analyses is the <code>run.analyse</code> function.
            </template>
            <template slot="tags">
            </template>
        </card>

        <card>
            <template slot="heading">
                Rest API
            </template>
            <template slot="text-body" class="text-sm">
                The dorina python API can be used to run local dorina queries. The
                central entry point for all analyses is the <code>run.analyse</code> function.
            </template>
        </card>

        <card>
            <template slot="heading">

            </template>
            <template slot="text-body">
                <table class="table table-striped">
                    <thead>
                    <tr>
                        <th><h3>List available datasets</h3></th>
                        <th></th>
                    </tr>
                    <tr>
                        <th>Resource</th>
                        <th>Description</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td><a href="#">GET
                            api/v1.0/genomes</a></td>
                        <td>List available genomes</td>
                    </tr>
                    <tr>
                        <td><a href="#">GET
                            api/v1.0/assemblies/:genome</a></td>
                        <td>List available assemblies for a genome</td>
                    </tr>
                    <tr>
                        <td><a href="#">GET
                            api/v1.0/regulators/:assembly</a></td>
                        <td>List available regulators for an assembly</td>
                    </tr>
                    </tbody>

                    <thead>
                    <tr>
                        <th><h3>Run search</h3></th>
                        <th></th>
                    </tr>
                    <tr>
                        <th>Resource</th>
                        <th>Description</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td><a href="#">POST
                            api/v1.0/search</a></td>
                        <td>Run a doRiNA search</td>
                    </tr>
                    </tbody>

                    <thead>
                    <tr>
                        <th><h3>Query job information</h3></th>
                        <th></th>
                    </tr>
                    <tr>
                        <th>Resource</th>
                        <th>Description</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td><a href="#">GET
                            api/v1.0/status/:uuid</a></td>
                        <td>Get the status for job :uuid</td>
                    </tr>
                    <tr>
                        <td><a href="#">GET
                            api/v1.0/result/:uuid</a></td>
                        <td>Get the result for job :uuid</td>
                    </tr>
                    </tbody>

                    <thead>
                    <tr>
                        <th><h3>Download data</h3></th>
                        <th></th>
                    </tr>
                    <tr>
                        <th>Resource</th>
                        <th>Description</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>
                            <a href="#">GET
                                api/v1.0/download/results/:uuid</a></td>
                        <td>Download all results for job :uuid</td>
                    </tr>
                    <tr>
                        <td>
                            <a href="#">GET
                                api/v1.0/download/regulator/:assembly/:name</a></td>
                        <td>Download the regulator :name for :assembly</td>
                    </tr>
                    </tbody>
                </table>

            </template>

        </card>

    </div>

</template>

<script>
    import Axios from '@/components/Axios.vue'
    import Card from '../views/templates/molecules/Card.vue'

    export default {
        name: 'home',
        components: {
            Axios,
            Card

        }
    }
</script>
<style></style>
