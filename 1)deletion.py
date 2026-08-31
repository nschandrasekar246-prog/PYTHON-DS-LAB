{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOSs+8+kgk4VCGHySdby55A",
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
        "<a href=\"https://colab.research.google.com/github/nschandrasekar246-prog/PYTHON-DS-LAB/blob/main/deletion.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "83jDb4OQcbPq",
        "outputId": "0f6f773a-bb18-419c-9f87-8d1dabbe7abc"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Before deletion:\n",
            "Mon\n",
            "Tue\n",
            "Wed\n",
            "After deletion:\n",
            "Mon\n",
            "Wed\n"
          ]
        }
      ],
      "source": [
        "class Node:\n",
        "    def __init__(self, data=None):\n",
        "        self.data = data\n",
        "        self.next = None\n",
        "\n",
        "\n",
        "class SLinkedList:\n",
        "    def __init__(self):\n",
        "        self.head = None\n",
        "\n",
        "    def Atbegining(self, data_in):\n",
        "        NewNode = Node(data_in)\n",
        "        NewNode.next = self.head\n",
        "        self.head = NewNode\n",
        "\n",
        "    def RemoveNode(self, Removekey):\n",
        "        HeadVal = self.head\n",
        "\n",
        "        # If list is empty\n",
        "        if HeadVal is None:\n",
        "            return\n",
        "\n",
        "        # If first node contains the key\n",
        "        if HeadVal.data == Removekey:\n",
        "            self.head = HeadVal.next\n",
        "            HeadVal = None\n",
        "            return\n",
        "\n",
        "        # Search for the node\n",
        "        while HeadVal is not None:\n",
        "            if HeadVal.data == Removekey:\n",
        "                break\n",
        "\n",
        "            Prev = HeadVal\n",
        "            HeadVal = HeadVal.next\n",
        "\n",
        "        # Key not found\n",
        "        if HeadVal is None:\n",
        "            return\n",
        "\n",
        "        # Remove the node\n",
        "        Prev.next = HeadVal.next\n",
        "        HeadVal = None\n",
        "\n",
        "    def listprint(self):\n",
        "        current = self.head\n",
        "\n",
        "        while current is not None:\n",
        "            print(current.data)\n",
        "            current = current.next\n",
        "\n",
        "\n",
        "# Create linked list\n",
        "list = SLinkedList()\n",
        "\n",
        "list.Atbegining(\"Wed\")\n",
        "list.Atbegining(\"Tue\")\n",
        "list.Atbegining(\"Mon\")\n",
        "\n",
        "print(\"Before deletion:\")\n",
        "list.listprint()\n",
        "\n",
        "list.RemoveNode(\"Tue\")\n",
        "\n",
        "print(\"After deletion:\")\n",
        "list.listprint()"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "hBBbdXf-dRdI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "32DDFHY4c8GA"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "4Ntls6iIc8uu"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
