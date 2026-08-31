{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO4R9plM/tWVbH917FN8q34",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/nschandrasekar246-prog/PYTHON-DS-LAB/blob/main/INSERTION_PY.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NKAbvlCrU6F1",
        "outputId": "d61a5699-be16-4070-add2-bf7cb9acb7fe"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "sun\n",
            "mon\n",
            "tue\n",
            "wed\n"
          ]
        }
      ],
      "source": [
        "class Node:\n",
        "    def __init__(self, dataval=None):\n",
        "        self.dataval = dataval\n",
        "        self.nextval = None\n",
        "\n",
        "\n",
        "class SLinkedList:\n",
        "    def __init__(self):\n",
        "        self.headval = None\n",
        "\n",
        "    def listprint(self):\n",
        "        printval = self.headval\n",
        "\n",
        "        while printval is not None:\n",
        "            print(printval.dataval)\n",
        "            printval = printval.nextval\n",
        "\n",
        "    def AtBeginning(self, newdata):\n",
        "        NewNode = Node(newdata)\n",
        "        NewNode.nextval = self.headval\n",
        "        self.headval = NewNode\n",
        "\n",
        "\n",
        "list = SLinkedList()\n",
        "\n",
        "list.headval = Node(\"mon\")\n",
        "e2 = Node(\"tue\")\n",
        "e3 = Node(\"wed\")\n",
        "\n",
        "list.headval.nextval = e2\n",
        "e2.nextval = e3\n",
        "\n",
        "list.AtBeginning(\"sun\")\n",
        "list.listprint()"
      ]
    }
  ]
}
