{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8e4fe55c-26a9-4033-9f72-0d8f627fa947",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], np.float64(4.0)], 'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], np.float64(6.666666666666667)], 'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], np.float64(2.581988897471611)], 'max': [[6, 7, 8], [2, 5, 8], np.int64(8)], 'min': [[0, 1, 2], [0, 3, 6], np.int64(0)], 'sum': [[9, 12, 15], [3, 12, 21], np.int64(36)]}\n"
     ]
    }
   ],
   "source": [
    "from mean_var_std import calculate\n",
    "\n",
    "def main():\n",
    "    # test input\n",
    "    data = [0,1,2,3,4,5,6,7,8]\n",
    "\n",
    "    # call the function\n",
    "    result = calculate(data)\n",
    "\n",
    "    # print result\n",
    "    print(result)\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a6bf9e5-67f3-4558-8a40-c07a4aafa3ad",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
