{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNtPeKbgUTBb1YB/Q2zUT6F",
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
        "<a href=\"https://colab.research.google.com/github/nschandrasekar246-prog/PYTHON-DS-LAB/blob/main/traversal_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lWkwiQPNhaPQ",
        "outputId": "26cb35c6-9505-40d5-b167-2b4a6d481639"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n"
          ]
        }
      ],
      "source": [
        "class Node:\n",
        "    def __init__(self, data):\n",
        "        self.data = data\n",
        "        self.next = None\n",
        "\n",
        "\n",
        "class LinkedList:\n",
        "    def __init__(self):\n",
        "        self.head = None\n",
        "\n",
        "    def printList(self):\n",
        "        temp = self.head\n",
        "\n",
        "        while temp:\n",
        "            print(temp.data)\n",
        "            temp = temp.next\n",
        "\n",
        "\n",
        "if __name__ == '__main__':\n",
        "\n",
        "    llist = LinkedList()\n",
        "\n",
        "    llist.head = Node(1)\n",
        "\n",
        "    second = Node(2)\n",
        "    third = Node(3)\n",
        "\n",
        "    llist.head.next = second\n",
        "    second.next = third\n",
        "\n",
        "    llist.printList()"
      ]
    }
  ]
}
