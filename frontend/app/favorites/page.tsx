"use client";

//Global
import React, { useEffect } from "react";
import { useRouter } from "next/navigation";

//Components
import { Breadcrumbs, BreadcrumbItem } from "@nextui-org/react";
import { Icons } from "@/components/Icons/Icons";

//Hooks
import { useTranslate } from "@/hooks/useTranslate";
import { useFavorites } from "@/hooks/useFavorites";
import { useTypedSelector } from "@/hooks/useReduxHooks";

//Utils
import { FAVORITES_ROUTE, SHOP_ROUTE } from "@/utils/Consts";

//Styles
import "./favorites.scss";

export default function Favorites() {
  const { isAuth, status: userStatus } = useTypedSelector(state => state.user),
    { status: favoritesStatus } = useTypedSelector(state => state.favorites);

  const { mainPageRoute, headerFavorites } = useTranslate();

  const { renderUserFavorites } = useFavorites();

  const { push } = useRouter();

  useEffect(() => {
    if (!isAuth && userStatus === "fulfilled") push(SHOP_ROUTE);
  }, [isAuth, userStatus, push]);

  if (!isAuth || favoritesStatus === "pending" || userStatus === "pending")
    return <Icons id="spiner" />;

  return (
    <main className="container mx-auto mt-[30px] mb-[30px] px-[28px] sm:px-0">
      <Breadcrumbs>
        <BreadcrumbItem href={SHOP_ROUTE}>{mainPageRoute}</BreadcrumbItem>

        <BreadcrumbItem href={FAVORITES_ROUTE}>
          {headerFavorites}
        </BreadcrumbItem>
      </Breadcrumbs>

      <div className="w-full mt-[25px]">{renderUserFavorites()}</div>
    </main>
  );
}
