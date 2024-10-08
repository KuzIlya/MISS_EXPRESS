"use client";

// Global
import React, {
  ChangeEvent,
  useEffect,
  useMemo,
  useState,
  useCallback,
} from "react";
import Image from "next/image";
import { useRouter } from "next/navigation";

// Components
import { Icons } from "@/components/Icons/Icons";
import { ModalChange } from "@/components/ModalChange/ModalChange";

// Utils
import { SHOP_ROUTE } from "@/utils/Consts";

// Hooks
import { useTranslate } from "@/hooks/useTranslate";
import { useTypedSelector } from "@/hooks/useReduxHooks";
import { useUserActions } from "@/hooks/useUserActions";

// Images
import profile from "../../public/assets/other/profile-photo.png";

// Styles
import "./profile.scss";
import { ICart } from "@/types/reduxTypes";
import { ISortConfig } from "@/types/componentTypes";

const Profile = () => {
  const { isAuth, userState, status, userOrders, userReviews } =
    useTypedSelector(state => state.user);

  const [isChange, setIsChange] = useState<boolean>(false),
    [value, setValue] = useState<string>(""),
    [sortConfig, setSortConfig] = useState<ISortConfig>({
      key: "created_date",
      direction: "desc",
    });

  const { push } = useRouter();

  const {
    onGetUser,
    onGetOrders,
    onGetReviews,
    returnUserOrders,
    returnUserReviews,
  } = useUserActions();
  const {
    profilePageAddress,
    profilePageCompany,
    profilePageOrders,
    profilePageReviews,
    orderPagePhone,
  } = useTranslate();

  useEffect(() => {
    onGetUser();
  }, [onGetUser]);

  useEffect(() => {
    if (!isAuth && status === "fulfilled") push(SHOP_ROUTE);
  }, [isAuth, status, push]);

  useEffect(() => {
    if (isAuth) {
      onGetOrders();
      onGetReviews();
    }
  }, [onGetOrders, onGetReviews, isAuth]);

  const handleChangeInput = useCallback(
    (e: ChangeEvent<HTMLInputElement>) => setValue(e.target.value),
    []
  );

  const sortOrders = useCallback((orders: ICart[], config: ISortConfig) => {
    return [...orders].sort((a, b) => {
      const aValue = a[config.key as keyof ICart];
      const bValue = b[config.key as keyof ICart];

      if (aValue && bValue) {
        if (aValue < bValue) return config.direction === "asc" ? -1 : 1;
        if (aValue > bValue) return config.direction === "asc" ? 1 : -1;
      }

      return 0;
    });
  }, []);

  const filteredAndSortedOrders = useMemo(() => {
    const filtered = userOrders.filter(order =>
      String(order.id).includes(value)
    );
    return sortOrders(filtered, sortConfig);
  }, [value, userOrders, sortConfig, sortOrders]);

  const handleSort = useCallback((key: ISortConfig["key"]) => {
    setSortConfig(prevSortConfig => ({
      key,
      direction:
        prevSortConfig.key === key && prevSortConfig.direction === "asc"
          ? "desc"
          : "asc",
    }));
  }, []);

  if (!userState) return <Icons id="spiner" />;

  return (
    <main className="profile-wrapper">
      <div className="profile-content">
        <div className="profile-content_header">
          <div className="profile-content_header-user">
            <Image src={profile} alt="profile-photo" width={200} height={200} />

            <div className="profile-content_header-user-data">
              <h5 className="profile-content_header-user-data-title">
                {userState.user.first_name} {userState.user.last_name}
              </h5>

              <div className="profile-content_header-user-data-blocks">
                <div className="profile-content_header-user-data-block">
                  <span className="profile-content_header-user-data-block-bold">
                    {profilePageCompany}:
                  </span>

                  <span className="profile-content_header-user-data-block-light">
                    {userState.company || "Не указана"}
                  </span>
                </div>

                <div className="profile-content_header-user-data-block">
                  <span className="profile-content_header-user-data-block-bold">
                    {orderPagePhone}:
                  </span>

                  <span className="profile-content_header-user-data-block-light">
                    {userState.phone_number}
                  </span>
                </div>

                <div className="profile-content_header-user-data-block">
                  <span className="profile-content_header-user-data-block-bold">
                    {profilePageAddress}:
                  </span>

                  <span className="profile-content_header-user-data-block-light">
                    {userState.address || "Не указан"}
                  </span>
                </div>
              </div>
            </div>
          </div>

          <button onClick={() => setIsChange(!isChange)}>
            <Icons id="pencil" />
          </button>
        </div>

        <div className="profile-content_orders">
          <div className="profile-content_orders-header">
            <h5 className="profile-content_orders-header-text">
              {profilePageOrders}
            </h5>

            <div className="search-wrapper">
              <Icons id="search2" />

              <input
                value={value}
                onChange={handleChangeInput}
                className="profile-content_orders-header-input"
                placeholder={"Поиск..."}
                type="search"
              />
            </div>
          </div>

          {returnUserOrders(filteredAndSortedOrders, handleSort)}
        </div>

        <div className="profile-content_reviews">
          <h5 className="profile-content_reviews-title">
            {profilePageReviews}
          </h5>

          {returnUserReviews(userReviews)}
        </div>
      </div>

      <ModalChange isChange={isChange} setIsChange={setIsChange} />
    </main>
  );
};

export default React.memo(Profile);
