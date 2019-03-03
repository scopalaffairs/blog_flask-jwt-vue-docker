<template>
    <div>
        <card>
            <template slot="heading">
                Acknowledgements
            </template>
        </card>

        <card>
            <template slot="text-body" class="text-sm">
                We would like to thank:
                <ul>
                    Anne Ammerstorfer for Carina's logo design
                </ul>
                <ul>Tobias Jakobi and Mike Rightmire, who contributed to the web
                    service deployment and infrastructure support
                </ul>
                <ul>Kai Blin, who developed most of DoRiNA and webdorina</ul>

                <p class="col-lg-8 justify-content-center">
                    If you are using Carina, please cite:

                    <br>
                    Britto-Borges, Thiago and Dieterich Christoph "Carina: a Web
                    Portal for Cardiovascular RNA Interactions Integrated to
                    Splicing"
                    <br><br>
                    Carina extends on DoRiNA and webdorina:<br>
                    Blin, Kai, et al. <a class="text-info"
                                         href="http://www.ncbi.nlm.nih.gov/pubmed/25416797">
                    "DoRiNA 2.0—upgrading the doRiNA database of
                    RNA interactions in post-transcriptional regulation." </a>
                    <a class="font-italic"> Nucleic acids research </a>
                    43.D1 (2014): D160-D167.
                    <br>
                    Anders, Gerd, et al. <a class="text-info"
                                            href="http://www.ncbi.nlm.nih.gov/pubmed/22086949">

                    "doRiNA: a database of RNA interactions in
                    post-transcriptional regulation."</a>
                    <a class="font-italic">Nucleic acids research</a>
                    40.D1 (2011): D180-D186.
                </p>

            </template>
            <template slot="tags">

            </template>

        </card>
    </div>
</template>

<script>
    // @ is an alias to /src
    import Axios from '../components/Axios.vue'
    import Card from '../views/templates/molecules/Card.vue'

    export default {
        name: 'home',
        components: {
            Axios,
            Card,

        }
    }
</script>
<style></style>
