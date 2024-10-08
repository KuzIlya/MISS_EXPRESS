"use client";

//Global
import { NextPage } from "next";
import React from "react";
import Link from "next/link";

//Hooks
import { useTranslate } from "@/hooks/useTranslate";

const SuccessfulPaymentPage: NextPage = () => {
  const { paymentSuccess, paymentSuccessText, paymentButton } = useTranslate();

  return (
    <div className="h-[358px] flex justify-center items-center flex-col gap-[40px]">
      <div className="flex flex-col gap-[20px]">
        <h5 className="text-tiffani text-center font-medium text-[50px]">
          {paymentSuccess}
        </h5>

        <p className="text-gray/500 text-[16px] text-center">
          {paymentSuccessText}
        </p>
      </div>

      <Link
        className="w-[187px] h-[44px] flex justify-center items-center bg-tiffani text-white rounded-[5px] py-[10px] px-[20px] text-[14px]"
        href="https://mis-express.com/"
      >
        {paymentButton}
      </Link>
    </div>
  );
};

export default SuccessfulPaymentPage;
