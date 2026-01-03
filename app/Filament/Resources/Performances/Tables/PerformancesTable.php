<?php

namespace App\Filament\Resources\Performances\Tables;

use Filament\Actions\BulkActionGroup;
use Filament\Actions\DeleteBulkAction;
use Filament\Actions\EditAction;
use Filament\Tables\Columns\IconColumn;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;

class PerformancesTable
{
    public static function configure(Table $table): Table
    {
        return $table
            ->columns([
                TextColumn::make('game_id')
                    ->numeric()
                    ->sortable(),
                TextColumn::make('player_id')
                    ->numeric()
                    ->sortable(),
                TextColumn::make('brawler_name')
                    ->searchable(),
                TextColumn::make('kills')
                    ->numeric()
                    ->sortable(),
                TextColumn::make('deaths')
                    ->numeric()
                    ->sortable(),
                TextColumn::make('damage_dealt')
                    ->numeric()
                    ->sortable(),
                TextColumn::make('damage_received')
                    ->numeric()
                    ->sortable(),
                TextColumn::make('damage_to_safe')
                    ->numeric()
                    ->sortable(),
                TextColumn::make('rating_bser')
                    ->numeric()
                    ->sortable(),
                IconColumn::make('is_win')
                    ->boolean(),
                TextColumn::make('created_at')
                    ->dateTime()
                    ->sortable()
                    ->toggleable(isToggledHiddenByDefault: true),
                TextColumn::make('updated_at')
                    ->dateTime()
                    ->sortable()
                    ->toggleable(isToggledHiddenByDefault: true),
            ])
            ->filters([
                //
            ])
            ->recordActions([
                EditAction::make(),
            ])
            ->toolbarActions([
                BulkActionGroup::make([
                    DeleteBulkAction::make(),
                ]),
            ]);
    }
}
