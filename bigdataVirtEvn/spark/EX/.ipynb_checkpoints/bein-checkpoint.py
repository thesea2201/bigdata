{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = spark.read.json(\"../examples/src/main/resources/people.json\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+----+-------+\n",
      "| age|   name|\n",
      "+----+-------+\n",
      "|null|Michael|\n",
      "|  30|   Andy|\n",
      "|  19| Justin|\n",
      "+----+-------+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "root\n",
      " |-- age: long (nullable = true)\n",
      " |-- name: string (nullable = true)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df.printSchema()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+-------+\n",
      "|   name|\n",
      "+-------+\n",
      "|Michael|\n",
      "|   Andy|\n",
      "| Justin|\n",
      "+-------+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df.select(\"name\").show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+-------+---------+\n",
      "|   name|(age + 1)|\n",
      "+-------+---------+\n",
      "|Michael|     null|\n",
      "|   Andy|       31|\n",
      "| Justin|       20|\n",
      "+-------+---------+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df.select(df['name'], df['age']+1).show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+---+----+\n",
      "|age|name|\n",
      "+---+----+\n",
      "| 30|Andy|\n",
      "+---+----+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df.filter(df['age']>20).show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+----+\n",
      "|name|\n",
      "+----+\n",
      "|Andy|\n",
      "+----+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df.filter(df['age']>20).select(\"name\").show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+----+-----+\n",
      "| age|count|\n",
      "+----+-----+\n",
      "|  19|    1|\n",
      "|null|    1|\n",
      "|  30|    1|\n",
      "+----+-----+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df.groupBy(\"age\").count().show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
