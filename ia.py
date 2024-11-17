{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/yxrellx/practicaredNeuronal/blob/main/ia.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**FRAME**"
      ],
      "metadata": {
        "id": "6pCx255bP6wm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import json\n",
        "\n",
        "# Cargar el archivo JSON en Colab\n",
        "with open('/content/datos.json', 'r') as file:\n",
        "    data = json.load(file)\n",
        "\n",
        "# Verificar el contenido del JSON\n",
        "print(json.dumps(data, indent=4))\n"
      ],
      "metadata": {
        "id": "j-6-JtLEe6S1",
        "outputId": "aba87dd2-0d7c-4878-8b80-768c0cdeeb5b",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{\n",
            "    \"personas\": [\n",
            "        {\n",
            "            \"nombre\": \"Juan\",\n",
            "            \"edad\": 30,\n",
            "            \"padre\": \"Carlos\",\n",
            "            \"color_favorito\": \"azul\"\n",
            "        },\n",
            "        {\n",
            "            \"nombre\": \"Mar\\u00eda\",\n",
            "            \"edad\": 25,\n",
            "            \"color_favorito\": \"verde\"\n",
            "        },\n",
            "        {\n",
            "            \"nombre\": \"Pedro\",\n",
            "            \"edad\": 35,\n",
            "            \"color_favorito\": \"rojo\"\n",
            "        },\n",
            "        {\n",
            "            \"nombre\": \"Laura\",\n",
            "            \"edad\": 40,\n",
            "            \"trabajo\": \"doctora\"\n",
            "        }\n",
            "    ],\n",
            "    \"animales\": [\n",
            "        {\n",
            "            \"nombre\": \"perro\",\n",
            "            \"patas\": 4,\n",
            "            \"color\": \"marr\\u00f3n\"\n",
            "        },\n",
            "        {\n",
            "            \"nombre\": \"gato\",\n",
            "            \"patas\": 4,\n",
            "            \"color\": \"gris\"\n",
            "        },\n",
            "        {\n",
            "            \"nombre\": \"p\\u00e1jaro\",\n",
            "            \"patas\": 2,\n",
            "            \"color\": \"amarillo\"\n",
            "        }\n",
            "    ]\n",
            "}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# Crear los frames para las personas\n",
        "personas_frames = []\n",
        "for persona in data['personas']:\n",
        "    frame = Frame(persona['nombre'])\n",
        "    frame.add_attribute(\"edad\", persona['edad'])\n",
        "\n",
        "    # Verificar si el atributo padre existe antes de agregarlo\n",
        "    if 'padre' in persona:\n",
        "        frame.add_attribute(\"padre\", persona['padre'])\n",
        "\n",
        "    # Verificar si el atributo trabajo existe antes de agregarlo\n",
        "    if 'trabajo' in persona:\n",
        "        frame.add_attribute(\"trabajo\", persona['trabajo'])\n",
        "\n",
        "    # Verificar si el atributo color_favorito existe antes de agregarlo\n",
        "    if 'color_favorito' in persona:\n",
        "        frame.add_attribute(\"color_favorito\", persona['color_favorito'])\n",
        "\n",
        "    personas_frames.append(frame)\n",
        "\n",
        "# Crear los frames para los animales\n",
        "animales_frames = []\n",
        "for animal in data['animales']:\n",
        "    frame = Frame(animal['nombre'])\n",
        "    frame.add_attribute(\"patas\", animal['patas'])\n",
        "    frame.add_attribute(\"color\", animal['color'])\n",
        "    animales_frames.append(frame)\n",
        "\n",
        "# Mostrar los datos estructurados de los frames\n",
        "for persona in personas_frames:\n",
        "    print(f\"Nombre: {persona.name}, Atributos: {persona.attributes}\")\n",
        "\n",
        "for animal in animales_frames:\n",
        "    print(f\"Nombre: {animal.name}, Atributos: {animal.attributes}\")"
      ],
      "metadata": {
        "id": "x0mnOTfKdRv1",
        "outputId": "a207570a-d3d8-4e07-ee9a-1f2ac8742d78",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Nombre: Juan, Atributos: {'edad': 30, 'padre': 'Carlos', 'color_favorito': 'azul'}\n",
            "Nombre: María, Atributos: {'edad': 25, 'color_favorito': 'verde'}\n",
            "Nombre: Pedro, Atributos: {'edad': 35, 'color_favorito': 'rojo'}\n",
            "Nombre: Laura, Atributos: {'edad': 40, 'trabajo': 'doctora'}\n",
            "Nombre: perro, Atributos: {'patas': 4, 'color': 'marrón'}\n",
            "Nombre: gato, Atributos: {'patas': 4, 'color': 'gris'}\n",
            "Nombre: pájaro, Atributos: {'patas': 2, 'color': 'amarillo'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**PREGUNTAS**\n"
      ],
      "metadata": {
        "id": "J5kB86xEQ4iW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import json"
      ],
      "metadata": {
        "id": "drqXVZuNSdGn"
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "padre_de_juan = df_personas[df_personas['nombre'] == 'Juan']['padre'].values[0]  #(en este caso, único) valor de la serie resultante\n",
        "print(f\"El padre de Juan es: {padre_de_juan}\")"
      ],
      "metadata": {
        "id": "13DBOBAPSmKN",
        "outputId": "56274790-b9b4-4634-8407-ca4b4061e780",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "El padre de Juan es: Carlos\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "color_favorito_maria = df_personas[df_personas['nombre'] == 'María']['color_favorito'].values[0]#(en este caso, único) valor de la serie resultante\n",
        "print(f\"El color favorito de María es: {color_favorito_maria}\")"
      ],
      "metadata": {
        "id": "E2ejHKeKSoDu",
        "outputId": "cbac543b-5271-467a-e0b2-1382fd680396",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "El color favorito de María es: verde\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "animales_cuatro_patas = [animal['nombre'] for animal in data['animales'] if animal['patas'] == 4]\n",
        "print(f\"Los animales con cuatro patas son: {', '.join(animales_cuatro_patas)}\")"
      ],
      "metadata": {
        "id": "Kj3eEytfS1FQ",
        "outputId": "45ea611f-72cc-4935-cc89-49fb03ed97cd",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Los animales con cuatro patas son: perro, gato\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "trabajo_de_laura = df_personas[df_personas['nombre'] == 'Laura']['trabajo'].values[0]#(en este caso, único) valor de la serie resultante\n",
        "print(f\"El trabajo de Laura es: {trabajo_de_laura}\")\n"
      ],
      "metadata": {
        "id": "SVZ8IhGTTKOG",
        "outputId": "f5d652f3-5aa3-425c-b5f0-8ae70fccee1b",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "El trabajo de Laura es: doctora\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "Te damos la bienvenida a Colaboratory",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}