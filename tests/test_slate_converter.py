# Based on the go-utils slate_converter_test https://github.com/kumparan/go-utils/blob/master/slate_converter_test.go

import unittest

from upils.slate_converter import SlateDocument, SlateLeaf, SlateNode


class SlateConverterCase(unittest.TestCase):
    def test_slateleaf_from_dict(self):
        input_dict = {
            "object": "leaf",
            "text": "ini adalah judul",
            "marks": [
                {"object": "mark", "type": "bold"},
                {"object": "mark", "type": "italic"},
                {"object": "mark", "type": "underline"},
            ],
        }
        expected_object = "leaf"
        expected_text = "ini adalah judul"
        expected_marks = [
            {"object": "mark", "type": "bold"},
            {"object": "mark", "type": "italic"},
            {"object": "mark", "type": "underline"},
        ]

        input = SlateLeaf.from_dict(input_dict)
        assert input is not None

        assert input.object == expected_object
        assert input.text == expected_text
        assert input.marks == expected_marks

    def test_slateleaf_from_dict_defaults(self):
        input_dict = {}
        expected_object = "leaf"
        expected_text = ""
        expected_marks = []

        input = SlateLeaf.from_dict(input_dict)
        assert input is not None

        assert input.object == expected_object
        assert input.text == expected_text
        assert input.marks == expected_marks

    def test_slatenode_from_dict_with_leaves(self):
        input_dict = {
            "object": "block",
            "type": "paragraph",
            "leaves": [
                {
                    "object": "leaf",
                    "text": "ini adalah judul",
                    "marks": [
                        {"object": "mark", "type": "bold"},
                        {"object": "mark", "type": "italic"},
                        {"object": "mark", "type": "underline"},
                    ],
                }
            ],
        }
        expected_object = "block"
        expected_type = "paragraph"
        expected_leaf_length = 1
        expected_leaf_text = "ini adalah judul"

        input = SlateNode.from_dict(input_dict)
        assert input is not None

        assert input.object == expected_object
        assert input.type == expected_type
        assert len(input.leaves) == expected_leaf_length
        assert input.leaves[0].text == expected_leaf_text

    def test_slatenode_from_dict_with_children(self):
        input_dict = {
            "object": "block",
            "type": "paragraph",
            "nodes": [
                {
                    "object": "block",
                    "type": "inline",
                    "leaves": [
                        {
                            "object": "leaf",
                            "text": "ini adalah judul",
                            "marks": [
                                {"object": "mark", "type": "bold"},
                                {"object": "mark", "type": "italic"},
                                {"object": "mark", "type": "underline"},
                            ],
                        }
                    ],
                }
            ],
        }
        expected_node_type = "paragraph"
        exptected_node_length = 1
        expected_node_children_type = "inline"
        expected_leaf_text = "ini adalah judul"

        input = SlateNode.from_dict(input_dict)
        assert input is not None

        assert input.type == expected_node_type
        assert len(input.nodes) == exptected_node_length
        assert input.nodes[0].type == expected_node_children_type
        assert input.nodes[0].leaves[0].text == expected_leaf_text

    def test_slatedocument_from_dict(self):
        input_dict = {
            "document": {
                "nodes": [
                    {
                        "object": "block",
                        "type": "paragraph",
                        "leaves": [
                            {
                                "object": "leaf",
                                "text": "ini adalah judul",
                                "marks": [
                                    {"object": "mark", "type": "bold"},
                                    {"object": "mark", "type": "italic"},
                                    {"object": "mark", "type": "underline"},
                                ],
                            }
                        ],
                    }
                ]
            }
        }
        expected_node_length = 1
        expected_first_node_type = "paragraph"
        expected_leaf_length = 1

        input = SlateDocument.from_dict(input_dict)
        assert input is not None

        assert len(input.nodes) == expected_node_length
        assert input.nodes[0].type == expected_first_node_type
        assert len(input.nodes[0].leaves) == expected_leaf_length

    def test_slatedocument_from_dict_defaults(self):
        input = SlateDocument.from_dict({})
        expected_node_length = 0
        assert len(input.nodes) == expected_node_length

    def test_to_plain_text(self):
        input_json = """{"document":{"nodes":[{"object":"block","type":"heading-large","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"10 HP Android Paling Ngebut Versi AnTuTu Februari 2025, Ini Juaranya","marks":[]}]}]},{"object":"block","type":"figure","data":{},"nodes":[{"object":"block","type":"image","data":{"image":{"id":"1741342849091738823","title":"Untitled Image","description":"","publicID":"01jnr1ydtm32jndtmgaytxzp4y","externalURL":"https://blue.kumparan.com/image/upload/v1634025439/01jnr1ydtm32jndtmgaytxzp4y.jpg","awsS3Key":"2025/Mar/image/01jnr1ydtm32jndtmgaytxzp4y/","height":433,"width":768,"locationName":null,"locationLat":0,"locationLon":0,"mediaType":"IMAGE","mediaSourceID":"7","photographer":"","eventDate":"2025-03-07T10:20:49.091685Z","internalTags":[],"__typename":"Media"}},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"","marks":[]}]}]},{"object":"block","type":"caption","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"OnePlus Ace 5 Pro. Foto: OnePlus","marks":[]}]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"Platform benchmark AnTuTu meluncurkan laporan baru soal daftar handphone (","marks":[]}]},{"object":"inline","type":"link","data":{"href":"https://kumparan.com/topic/hp"},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"HP","marks":[]}]}]},{"object":"text","leaves":[{"object":"leaf","text":") Android dengan performa terkencang di dunia. Untuk periode Februari 2025, smartphone dengan dapur pacu Snapdragon 8 Elite menjadi juaranya.","marks":[]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"Pengukuran AnTuTu berdasarkan beberapa aspek komponen di ","marks":[]}]},{"object":"inline","type":"link","data":{"href":"https://kumparan.com/topic/smartphone"},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"smartphone","marks":[]}]}]},{"object":"text","leaves":[{"object":"leaf","text":", seperti CPU, GPU, RAM, memori penyimpanan, hingga UX. Skor yang ditampilkan merupakan hasil sejumlah pengujian benchmark perangkat via aplikasi AnTuTu, minimal 1.000 kali dalam sebulan","marks":[]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"Prosesor Snapdragon 8 Elite dari Qualcomm dan Dimensity 9400 buatan MediaTek bersaing ketat dalam daftar 10 HP ","marks":[]}]},{"object":"inline","type":"link","data":{"href":"https://kumparan.com/topic/android"},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"Android","marks":[]}]}]},{"object":"text","leaves":[{"object":"leaf","text":" dengan performa tercepat selama Februari 2025. Berikut daftar lengkapnya:","marks":[]}]}]},{"object":"block","type":"numbered-list","data":{},"nodes":[{"object":"block","type":"list-item","data":{},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"OnePlus Ace 5 Pro","marks":[]}]}]}]},{"object":"block","type":"list-item","data":{},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"vivo X200 Pro","marks":[]}]}]}]},{"object":"block","type":"list-item","data":{},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"Red Magic 10 Pro+","marks":[]}]}]}]},{"object":"block","type":"list-item","data":{},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"iQoo 13","marks":[]}]}]}]},{"object":"block","type":"list-item","data":{},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"iQoo Neo 10 Pro","marks":[]}]}]}]},{"object":"block","type":"list-item","data":{},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"OnePlus 13","marks":[]}]}]}]},{"object":"block","type":"list-item","data":{},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"Realme GT 7 Pro","marks":[]}]}]}]},{"object":"block","type":"list-item","data":{},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"Oppo Find X8 Pro","marks":[]}]}]}]},{"object":"block","type":"list-item","data":{},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"Redmi K80 Pro","marks":[]}]}]}]},{"object":"block","type":"list-item","data":{},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"Oppo Find X8","marks":[]}]}]}]}]},{"object":"block","type":"figure","data":{},"nodes":[{"object":"block","type":"image","data":{"image":{"id":"1741342007934594403","title":"Untitled Image","description":"","publicID":"01jnr14renhw6ssnzjpd824eb7","externalURL":"https://blue.kumparan.com/image/upload/v1634025439/01jnr14renhw6ssnzjpd824eb7.jpg","awsS3Key":"2025/Mar/image/01jnr14renhw6ssnzjpd824eb7/","height":556,"width":738,"locationName":null,"locationLat":0,"locationLon":0,"mediaType":"IMAGE","mediaSourceID":"7","photographer":"","eventDate":"2025-03-07T10:06:47.934489Z","internalTags":[],"__typename":"Media"}},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"","marks":[]}]}]},{"object":"block","type":"caption","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"Daftar 10 HP Android flagship paling ngebut versi AnTuTu periode Februari 2025. Foto: AnTuTu","marks":[]}]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"Peringkat pertama ditempati OnePlus Ace 5 Pro berbasis Snapdragon 8 Elite, dengan skor AnTuTu mencapai 2.890.600. Sementara itu, runner up-nya adalah vivo X200 Pro yang menggunakan cip Dimensity 9400, dengan skor AnTuTu 2.884.682.","marks":[]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"RedMagic 10 Pro+ berada di posisi ketiga dengan skor AnTuTu 2.879.356, diikuti oleh iQoo 13 di peringkat keempat dengan skor AnTuTu 2.853.651. Kemudian, peringkat top 5 terakhir ditempati oleh iQoo Neo 10 Pro dengan skor AnTuTu 2.836.633.","marks":[]}]}]}]}}"""

        expected = """Platform benchmark AnTuTu meluncurkan laporan baru soal daftar handphone (HP) Android dengan performa terkencang di dunia. Untuk periode Februari 2025, smartphone dengan dapur pacu Snapdragon 8 Elite menjadi juaranya.
Pengukuran AnTuTu berdasarkan beberapa aspek komponen di smartphone, seperti CPU, GPU, RAM, memori penyimpanan, hingga UX. Skor yang ditampilkan merupakan hasil sejumlah pengujian benchmark perangkat via aplikasi AnTuTu, minimal 1.000 kali dalam sebulan.
Prosesor Snapdragon 8 Elite dari Qualcomm dan Dimensity 9400 buatan MediaTek bersaing ketat dalam daftar 10 HP Android dengan performa tercepat selama Februari 2025. Berikut daftar lengkapnya:
OnePlus Ace 5 Pro, vivo X200 Pro, Red Magic 10 Pro+, iQoo 13, iQoo Neo 10 Pro, OnePlus 13, Realme GT 7 Pro, Oppo Find X8 Pro, Redmi K80 Pro, Oppo Find X8. Peringkat pertama ditempati OnePlus Ace 5 Pro berbasis Snapdragon 8 Elite, dengan skor AnTuTu mencapai 2.890.600. Sementara itu, runner up-nya adalah vivo X200 Pro yang menggunakan cip Dimensity 9400, dengan skor AnTuTu 2.884.682.
RedMagic 10 Pro+ berada di posisi ketiga dengan skor AnTuTu 2.879.356, diikuti oleh iQoo 13 di peringkat keempat dengan skor AnTuTu 2.853.651. Kemudian, peringkat top 5 terakhir ditempati oleh iQoo Neo 10 Pro dengan skor AnTuTu 2.836.633."""

        input = SlateDocument.parse(input_json)
        assert input is not None

        result = input.to_plain_text()
        assert result == expected

    def test_text_link_not_contain_space(self):
        input_json = """{"document":{"nodes":[{"object":"block","type":"heading-large","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"ini adalah judul","marks":[]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"tanda kemunculan ","marks":[]}]},{"object":"inline","type":"link","data":{"href":"https://kumparan.com"},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"suzuki fronx","marks":[]}]}]},{"object":"text","leaves":[{"object":"leaf","text":" di indonesia.","marks":[]}]}]}]}}"""
        expected = "tanda kemunculan suzuki fronx di indonesia."

        input = SlateDocument.parse(input_json)
        assert input is not None

        result = input.to_plain_text()
        assert result == expected

    def test_text_link_include_space_on_prefix(self):
        input_json = """{"document":{"nodes":[{"object":"block","type":"heading-large","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"ini adalah judul","marks":[]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"tanda kemunculan","marks":[]}]},{"object":"inline","type":"link","data":{"href":"https://kumparan.com"},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":" suzuki fronx","marks":[]}]}]},{"object":"text","leaves":[{"object":"leaf","text":" di indonesia.","marks":[]}]}]}]}}"""
        expected = "tanda kemunculan suzuki fronx di indonesia."

        input = SlateDocument.parse(input_json)
        assert input is not None

        result = input.to_plain_text()
        assert result == expected

    def test_text_link_include_space_on_suffix(self):
        input_json = """{"document":{"nodes":[{"object":"block","type":"heading-large","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"ini adalah judul","marks":[]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"tanda kemunculan ","marks":[]}]},{"object":"inline","type":"link","data":{"href":"https://kumparan.com"},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"suzuki fronx ","marks":[]}]}]},{"object":"text","leaves":[{"object":"leaf","text":"di indonesia.","marks":[]}]}]}]}}"""
        expected = "tanda kemunculan suzuki fronx di indonesia."

        input = SlateDocument.parse(input_json)
        assert input is not None

        result = input.to_plain_text()
        assert result == expected

    def test_text_link_include_space_on_prefix_and_suffix(self):
        input_json = """{"document":{"nodes":[{"object":"block","type":"heading-large","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"ini adalah judul","marks":[]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"tanda kemunculan","marks":[]}]},{"object":"inline","type":"link","data":{"href":"https://kumparan.com"},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":" suzuki fronx ","marks":[]}]}]},{"object":"text","leaves":[{"object":"leaf","text":"di indonesia.","marks":[]}]}]}]}}"""
        expected = "tanda kemunculan suzuki fronx di indonesia."

        input = SlateDocument.parse(input_json)
        assert input is not None

        result = input.to_plain_text()
        assert result == expected

    def test_text_with_all_types_of_marks(self):
        input_json = """{"document":{"nodes":[{"object":"block","type":"heading-large","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"title ","marks":[]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"bold","marks":[{"object":"mark","type":"bold"}]},{"object":"leaf","text":" pada awal kalimat, kemudian ","marks":[]},{"object":"leaf","text":"italic","marks":[{"object":"mark","type":"italic"}]},{"object":"leaf","text":" dan ","marks":[]},{"object":"leaf","text":"underline","marks":[{"object":"mark","type":"underline"}]},{"object":"leaf","text":" pada tengah kalimat, serta pada akhir kalimat ","marks":[]},{"object":"leaf","text":"semuanya","marks":[{"object":"mark","type":"bold"},{"object":"mark","type":"italic"},{"object":"mark","type":"underline"}]}]}]}]}}"""
        expected = "bold pada awal kalimat, kemudian italic dan underline pada tengah kalimat, serta pada akhir kalimat semuanya."

        input = SlateDocument.parse(input_json)
        assert input is not None

        result = input.to_plain_text()
        assert result == expected


if __name__ == "__main__":
    unittest.main()
